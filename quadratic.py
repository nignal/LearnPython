# -*- coding: utf-8 -*-

import math
a = int(input ('a='))
b = int(input ('b='))
c = int(input ('c='))
def quadratic(a,b,c):
	x1 = (-b + math.sqrt(b*b-4*a*c))/(2*a)
	x2 = (-b - math.sqrt(b*b-4*a*c))/(2*a)
	print (x1,x2)

quadratic (a,b,c)