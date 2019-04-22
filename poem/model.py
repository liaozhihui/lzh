# coding=utf-8
import tensorflow as tf
import numpy as np

def rnn_model(model,input_data,output_data,vocab_size,\
              rnn_size=128,num_layers=2,batch_size=64,learning_rate=0.01):
    end_points= {}

    def rnn_cell():

        if model=='run':
            cell_fun = tf.contrib.rnn.BasicRNNCell
        elif model=='gru':
            cell_fun = tf.contrib.rnn.GRUCell
        elif model=='lstm':
            cell_fun=tf.contrib.rnn.BasicLSTMCell

        cell_fun=cell_fun(rnn_size,state_is_tuple=True)
        return cell_fun
    cell=tf.contrib.rnn.MultiRNNCell([rnn_cell() for _ in range(num_layers)],state_is_tuple=True)

    if output_data is not None:
        initial_state = cell.zero_state(batch_size=batch_size,dtype=tf.float32)

    else:
        initial_state = cell.zero_state(1, dtype=tf.float32)

    with tf.device("/cpu:0"):
        embeding= tf.get_variable('embeding',initializer=tf.random.uniform([vocab_size+1,rnn_size],-1.0,1.0))
        inputs = tf.nn.embedding_lookup(embeding,input_data) #128

    outputs,last_state=tf.nn.dynamic_rnn(cell,inputs,initial_state = initial_state)

    output=tf.reshape(outputs,[-1,rnn_size])

    weights=tf.Variable(tf.truncated_normal(rnn_size,vocab_size+1))
    bias = tf.Variable(tf.zeros(shape=[vocab_size+1]))
    logits = tf.nn.bias_add(tf.matmul(output,weights),bias=bias)

    if output_data is not None:
        labels = tf.one_hot(tf.reshape(output_data,[-1]),depth=vocab_size+1)
        loss=tf.nn.softmax_cross_entropy_with_logits_v2(labels=labels,logits=logits)

        total_loss = tf.reduce_mean(loss)
        train_op=tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(total_loss)
        end_points['initial_state'] = initial_state
        end_points['output'] = output
        end_points['train_op'] = train_op
        end_points['total_loss'] = total_loss
        end_points['loss'] = loss
        end_points['last_state'] = last_state
    else:
        prediction = tf.nn.softmax(logits)

        end_points['initial_state'] = initial_state
        end_points['last_state'] = last_state
        end_points['prediction'] = prediction

    return end_points
