import gevent

def foo():
	print("running foo")
	gevent.sleep(3)
	print("foo again")

def bar():
	print("running bar")
	gevent.sleep(2)
	print("bar again")

f = gevent.spawn(foo)

b=gevent.spawn(bar)
gevent.joinall([f,b])
