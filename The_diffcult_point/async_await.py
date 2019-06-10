# coding=utf-8
#python为了将语义变得更加明确，就引入了async和await关键词用于定义原生的协程

async def download(url):
    return "bobby"

async def download_url(url):
    #dosomethings
    html = await download(url)

    return html

if __name__ == '__main__':
    coro = download_url("http://www.imooc.com")
    # next(coro)
    coro.send(None)