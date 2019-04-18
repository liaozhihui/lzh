#计算密集型 x,y传入1
def count(x,y):
    c = 0
    while c < 7000000:
        c += 1
        x += 1
        y += 1

#io秘籍

def write():
    f = open("test",'w')
    for i in range(1200000):
        f.write("hello world\n")
    f.close()

def read():
    f = open("test")
    lines = f.readlines()
    f.close()

