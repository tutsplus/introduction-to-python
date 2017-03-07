
def numbers(limit):
	num = 0
	while(num <= limit):
		print(num)
		num += 1

def call_numbers(num_function, limit):
	num_function(limit)
	

func = numbers
upper = 15

call_numbers(func, upper)