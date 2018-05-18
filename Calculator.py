''' Calculator'''

#Arithmetic
def _arithmetic(oper1,oper2)
	print("Adition option 1")
	print("Subtraction option 2")
	print("Multiplication option 3")
	print("Division option 4")
	print("Modulus option 5")
	print("Exponent option 6")
	print("DFloor Division option 7")
	option=int(input('Please enter the option'))
	# Addition
	if option==1:
		print('{} + {} = '.format(number_1, number_2))
		print(number_1 + number_2)
	elif option==2:
		print('{} - {} = '.format(number_1, number_2))
		print(number_1 - number_2)
	elif option==3:
		print('{} * {} = '.format(number_1, number_2))
		print(number_1 * number_2)
	elif option==4:
		print('{} / {} = '.format(number_1, number_2))
		print(number_1 / number_2)
	elif option==5:
		print('{} % {} = '.format(number_1, number_2))
		print(number_1 % number_2)
	elif option==6:
		print('{} ** {} = '.format(number_1, number_2))
		print(number_1 ** number_2)
	elif option==7:
		print('{} // {} = '.format(number_1, number_2))
		print(number_1 // number_2)
	else:
		print('You did not enter the valid option')


