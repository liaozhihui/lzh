from threading import Event

#创建事件对象
e=Event()
e.set()  #设置e
e.clear() #清楚set状态
e.wait()

print("888888888888888")