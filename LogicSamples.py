def test(weekday, holiday):
	if not weekday:
		print("Weekday")
	if holiday:
		print("Holiday")
	

#test(True, True)
#test(True, False)
#test(False, True)


def string_explosion(string):
	print(string.count)
	for c in string:
		print(c + " ")

#string_explosion("string_explosion")


def substring(string):
	str = ""
	for x in range(len(string) + 1):
		str = str+string[:x]
	print(str)

#substring("Test")

def substrcount(string):
	substr = string[:2]
	print(string.count(substr))
	print(string[len(string)-2:len(string)])
	print(substr)
	
#substrcount("TeTest")

def near_hundred(n):
  if (abs(n - 100)) <= 10 or (abs(n - 200)) <= 10:
	print(abs(n- 100))
	return True
  else:
    return False


#near_hundred(89)

def test_string(test_input1, test_input2):
	length = len(test_input1) if len(test_input1) > len(test_input2) else len(test_input2)
	print(length)
	for i in range(length - 1):
		print(test_input1[i:i+2] + " " +  test_input2[i:i+2])

#test_string("can_breathe", "can_breathe12")


def test_string_by_two(test_input1):
	for i in range(len(test_input1)):
		if i%2 == 0:
			print(test_input1[i:i+1])

#test_string_by_two("paramore")


def test_make_bricks(small, big, goal):
	print (goal/  5)
	print (small + ( big * 5) >= goal and (goal/5) * 5) + small >= goal
	#return ((goalByFive * 5) + small) >= goal
	
	

#print(test_make_bricks(2 ,2, 8))

def make_chocolate(small, big, goal):
	print(small + ( big * 5 ) ) 
	if ( small + ( big * 5 ) ) >= goal:
		print( small - ( goal - (big * 5)) % small )
	else:
		print -1


make_chocolate(6, 2, 7)
make_chocolate(4, 1, 9)
make_chocolate(6, 2, 7) 