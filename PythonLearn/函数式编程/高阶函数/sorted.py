# -*- coding: utf-8 -*-

print sorted([36, 5, 12, 9, 21])		#[5, 9, 12, 21, 36]

def reverse_cmp(x, y):
	if x > y:
		return -1
	elif x < y:
		return 1
	return 0
print sorted([36, 5, 12, 9, 21], reverse_cmp)	#[36, 21, 12, 9, 5]

print sorted(['bob', 'about', 'Zoo', 'Credit'])	#['Credit', 'Zoo', 'about', 'bob']

