
def get_average(number_list):
	total = 0
	list_len = len(number_list)
	
	if list_len == 0:
		return total
	
	for num in number_list:
		total += num
		
	return total / list_len


numbers = []

while(True):
	val = input("Please enter a number (q to quit): ")
	
	if val != 'q':
		numbers.append(int(val))
	else:
		break

avg = get_average(numbers)

print()
print("The average of the numbers is", avg)