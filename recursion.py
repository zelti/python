def factorial(number):
	if(number == 0):
		return 1
	
	return factorial(number-1) * number

if __name__ == '__main__':
	number = int(input('Ingrese el numero'))
	result = factorial(number)
	print('el factorial de {} es igual a {}'.format(number, result))
