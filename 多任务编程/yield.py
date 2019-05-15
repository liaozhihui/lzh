# coding=utf-8

def fun():
    print("启动生成器")
    yield 1
    print("生成器完成")
    yield 12
g = fun()
print(next(g))
print(next(g))
g.close()