#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def printHead(str):
	print(str)
	print('--------------------------------------------')

def printEnd():
	print('--------------------------------------------')
	print()
	print()
	print()




#dict & set
printHead('dict & set')

d = {
    'Michael': 95,
    'Bob': 75,
    'Tracy': 85
}
print('d[\'Michael\'] =', d['Michael'])
print('d[\'Bob\'] =', d['Bob'])
print('d[\'Tracy\'] =', d['Tracy'])
print('d.get(\'Thomas\', -1) =', d.get('Thomas', -1))
print()


s1 = set([1, 1, 2, 2, 3, 3])
print(s1)
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)

printEnd()





#函数
printHead('函数')
print('abs(100) =', abs(-100) )
print('max(2, 3, -1, 5) =', max(2, 3, -1, 5) )
print('int(12.34) =', int(12.34) )
print('str(123) =', str(123) )
print('bool(1) =', bool(1) )

def this_function_has_nothing_to_do():
	pass

def my_abs(x):#避免参数类型错误的abs方法
	if not isinstance(x, (int, float)):
		raise TypeError('bad oprand type')
	if x > 0:
		return x
	else:
		return -x
#my_abs('abc')
my_abs(-111)

import math

def move(x, y, step, angle = 0): #函数可以返回多个值
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx, ny
x, y = move(100, 100, 70, math.pi / 6)
print(x, y)
r = move(100, 100, 60, math.pi / 6)#返回的是一个tuple
print(r)

printEnd()





#切片&迭代
printHead('切片&迭代')

d = [1, 2, 3, 4, 5, 6]
print('d[0 : 3] =', d[0 : 3])
print('d[-3 : ] =', d[-3 : ])
print('\'ABCDEF\'[1 : 3] =', 'ABCDEF'[1 : 3])
print()

from collections import Iterable
print('str是否可迭代:', isinstance('abc', Iterable))
print('list是否可迭代:', isinstance([1, 2, 3], Iterable))
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)

printEnd()





#列表生成式&生成器&迭代器
print('列表生成式&生成器&迭代器')

print('[x * x for x in range(1, 11)] =', [x * x for x in range(1, 11)])
print('[x * x for x in range(1, 11) if x % 2 == 0] =', [x * x for x in range(1, 11) if x % 2 == 0])
print('[m + n for m in \'ABC\' for n in \'abc\'] =', [m + n for m in 'ABC' for n in 'abc'])
d = {'x': 'A', 'y': 'B', 'z': 'C' }
print([k + '=' + v for k, v in d.items()])

g = (x * x for x in range(6))
print([next(g) for i in range(6)])
def triangles():
    L1 = [1]
    L2 = []
    for i in range(1, 11):
        yield L1#这表示这个函数是一个generator
        L2 = [1]
        for j in range(i - 1):
            L2.append(L1[j] + L1[j + 1])
        L2.append(1)
        L1 = L2
n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break