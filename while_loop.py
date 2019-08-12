#looping in python
max = -999999999

# get the first value
number = int(input("Enter value or -1 to stop: "))

while number != -1:
	if number > max:
		max = number
	
	number = int(input("Enter value or -1 to stop: "))

print("The largest number is: ", max)