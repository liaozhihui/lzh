# coding=utf-8
#生成器是可以暂停的函数

import inspect

# def gen_func():
#     #第一返回值给调用方,第二调用方通过send方式传递值给gen
#     yield 1
#     return 'bobby'

#用同步的方式编写异步的代码,在适当的时候暂停函数并在适当的时候启动函数

def downloader(url):
    pass

def download_html(html):
    html = yield from downloader()


if __name__ == '__main__':
    gen=gen_func()
    print(inspect.getgeneratorstate(gen))
    next(gen)
    print(inspect.getgeneratorstate(gen))
    try:
        next(gen)
    except StopIteration:
        pass
    print(inspect.getgeneratorstate(gen))



