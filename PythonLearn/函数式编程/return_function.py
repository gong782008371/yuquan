# -*- coding: utf-8 -*-

#如果不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？
#相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）
def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax = ax + n
		return ax
	return sum
f = lazy_sum(1, 3, 4, 5, 6, 7)
print f 		#<function sum at 0x0000000002523748>
print f()		#26

f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print f1==f2	#False
