# -*- coding: utf-8 -*-

#由于函数也是一个对象，而且函数对象可以被赋值给变量
def now():
	print '2013-12-25'
f = now
f()		#2013-12-25


#函数对象有一个__name__属性，可以拿到函数的名字：
print f.__name__		#now


#现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，
#但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
def log(func):
	def wrapper(*args, **kw):
		print 'call %s():' % func.__name__
		return func(*args, **kw)
	return wrapper
#观察上面的log，因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数。
#我们要借助Python的@语法，把decorator置于函数的定义处：
@log
def currentTime():
	print '2013-12-25\n'
currentTime()   #call currentTime():
				#2013-12-25


#如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。
#比如，要自定义log的文本：
def log1(text):
	def decorator(func):
		def wrapper(*args, **kw):
			print '%s %s():' % (text, func.__name__)
			return func(*args, **kw)
		return wrapper
	return decorator
@log1('running')  #这里的‘running’就是参数
def buildFile(filename):
	print 'building file:%s\n' % filename
@log1('executing') #这里的‘execute’是参数
def executeFile(filename):
	print 'execute file:%s\n' % filename
buildFile('a.cpp')
executeFile('a.cpp')


#测试同一个函数可以实现打印日志或不打印日志
def sayHello():
	print 'hello world!\n'
func_with_log = log1('execute')(sayHello)	#定义一个打印日志信息的sayhello函数
func_without_log = sayHello					#定义一个不打印日志信息的sayHello函数
#这个函数运行时会打印出日志信息
func_with_log()			#execute sayHello:
						#hello world!
#这个函数运行时不会打印出日志信息
func_without_log()		#hello world!


print func_with_log.__name__	#wrapper	这里本来应该是sayHello，却因为装饰的原因变成了wrapper
								#因此需要想办法改回去：这里就用到了@functools.wraps语法：
#一个完整的decorator写法如下(带参数的)：
import functools
def log4func(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print '%s %s():' % (text, func.__name__)
			return func(*args, **kw)
		return wrapper
	return decorator
new_func = log4func('execute')(sayHello)
new_func()


#练习
#
#再思考一下能否写出一个@log的decorator，使它既支持：@log,又支持：@log('execute')

def log(arg):
	if hasattr(arg, '__call__'):    #表示arg是一个函数
		@functools.wraps(arg)
		def wrapper(*args, **kw):
			print 'execute %s():' % arg.__name__
			return arg(*args, **kw)
		return wrapper

	else:							#否则不是一个函数，再封装一层
		def decorator(func):
			@functools.wraps(func)
			def wrapper(*args, **kw):
				print '%s %s():' % (arg, func.__name__)
				return func(*args, **kw)
			return wrapper
		return decorator

def f():
	pass

f1 = log(f)
f2 = log('running')(f)

f1()	#execute f():    这里使用默认的execute
f2()	#running f():	 这里使用自定义的running
