# -*- coding: utf-8 -*-

f = abs
print f(-10) 			#10

def add(a, b, f):
	return f(a) + f(b)

print add(1, -4, abs)	#5
