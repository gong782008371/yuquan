# -*- coding:utf-8 -*-

#Python内建的filter()函数用于过滤序列。
#
#和map()类似，filter()也接收一个函数和一个序列。
#和map()不同的时，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

def is_odd(n):
	return n % 2 == 1
print filter(is_odd, [1, 2, 3, 4, 5, 6, 9])				#[1, 3, 5, 9]

def not_empty(s):
	return s and s.strip()
print filter(not_empty, ['A', '', 'B', None, 'C', '  ']) #['A', 'B', 'C']


#练习
#
#请尝试用filter()删除1~100的素数。

import math
def not_prime(x):
	if x <= 1:
		return True
	for i in range(2, int(math.sqrt(x + 0.5)) + 1):
		if x % i == 0:
			return True
	return False
print filter(not_prime, [i for i in range(1, 101)])