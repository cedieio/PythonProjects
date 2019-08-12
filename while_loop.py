#looping in python
max = -999999999

# get the first value
number = int(input("Enter value or -1 to stop: "))

# the loop
while number != -1:
	# check if the input is bigger than the max number and replace it if true
	if number > max:
		# replace max with the input
		max = number
	
	# ask again if condition is not met ( e.g. number is not -1)
	number = int(input("Enter value or -1 to stop: "))

# print the result
print("The largest number is: ", max)