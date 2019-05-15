# coding=utf-8
import asyncio

async def execute(x):
    print("Number",x)
coroutine=execute(1)
print("Coroute:",coroutine)
print("After calling execute")
task=asyncio.ensure_future(coroutine)
print('Task:',task)
loop = asyncio.get_event_loop()
loop.run_until_complete(task)
print('Task:',task)
print('After calling loop')