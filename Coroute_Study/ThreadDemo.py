# coding=utf-8
from  threading import Thread
import requests
import time
start=time.time()
def request():
    url = 'http://127.0.0.1:5000'
    print("Waiting for", url)
    response = requests.get(url).text
    print("Get response from", url, "Result:", response)

Threads=[]
for i in range(100):
   t=Thread(target=request)
   Threads.append(t)
   t.start()
for i in Threads:
    i.join()
end=time.time()
print("共耗时%s"%(end-start))



