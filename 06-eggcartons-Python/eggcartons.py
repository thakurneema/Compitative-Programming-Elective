# Write the function eggCartons(eggs) that takes 
# a non-negative integer number of eggs, and returns 
# the smallest integer number of cartons required to hold 
# that many eggs, where a carton may hold up to 12 eggs

# (fun_eggcartons(0), 0), (fun_eggcartons(12), 1),
#     (fun_eggcartons(10), 1), (fun_eggcartons(13), 2),
#     (fun_eggcartons(24), 2), (fun_eggcartons(25), 3)


def fun_eggcartons(eggs):
	# your code goes here
	if(eggs%12 == 0):
		return eggs//12
	else:
		return eggs//12 +1
