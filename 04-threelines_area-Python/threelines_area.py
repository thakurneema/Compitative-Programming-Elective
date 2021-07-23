# Write the function fun_threelines_area(d1, d2, d3) 
# that takes length of 3 sides
# find the area of a triangle(return an int) given its side lengths.

import math

def fun_threelines_area(a,b,c):
    total = (a+b+c)/2
    sum = total*(total-a)*(total-b)*(total-c)
    area = int(math.sqrt(sum))
    return area 
	
