# -*- encoding: utf-8 -*-


#map()函数接收两个参数，一个是函数，一个是序列
#map将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回。
def f(x):
	return x * x
print map(f, [1, 2, 3, 4, 5])					#[1, 4, 9, 16, 25]
print map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])		#['1', '2', '3', '4', '5', '6', '7', '8', '9']



#reduce把一个函数作用在一个序列[x1, x2, x3...]上，这个函数必须接收两个参数
#reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

def mul(a, b):
	return a * b
print reduce(mul, [1, 2, 3, 4, 5])		#120

def fn(a, b):
	return a * 10 + b
print reduce(fn, [1, 3, 5, 7, 9])		#13579

def char2num(s):
	return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
print reduce(fn, map(char2num, '13579'))#13579(实现将字符串转化为整数)

def str2int(s):#上述功能的另一种写法
	return reduce(lambda x, y: x * 10 + y, map(char2num, s))
print str2int('13579')


#练习
#
#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
#输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']。
#
#Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积。

def trans(s):
	return s[0].upper() + s[1:].lower()
print map(trans, ['adam', 'LISA', 'barT'])

def prod(l):
	return reduce(lambda x, y: x * y, l)
print prod([1, 2, 3, 4, 5, 6])