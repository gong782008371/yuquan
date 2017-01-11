# -*- coding: utf-8 -*-

import functools

#简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），
#返回一个新的函数，调用这个新函数会更简单。
int2 = functools.partial(int, base=2) #将字符串按二进制读取转化为十进制
print int2('100000')
print int2('101010')


#partial实际上可以接收函数对象、*args和**kw这3个参数
int3 = functools.partial(int, '120', base = 3)
print int3()

my_max = functools.partial(max, 1000, 100) #这里的1000,100本作为my_max的两个参数
print my_max()		#1000    默认是含有上述的两个参数的
print my_max(11111) #11111   相当于三个数相比较
print my_max(500)   #1000    三个参数比较最大值
