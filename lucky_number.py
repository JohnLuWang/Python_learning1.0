lucky_number=10
num=-1
while lucky_number!=num:
	num=int(input("the number you input is:"))
	if num>lucky_number:
		print("the real number is smaller")
	elif num<lucky_number:
		print("the real number is bigger")
print("bingo!")