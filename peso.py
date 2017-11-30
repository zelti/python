def exchange_calculator(amount):
	cl_to_bs = 120
	return amount * cl_to_bs

def run():
	print('CALCULADORA DE DIVISAS')
	print('pesos chilenos a bolivares')
	print('')

	amount = float(input('Indique la cantidad de pesos a cambiar'))
	result = exchange_calculator(amount)

	print('${} pesos chilenos son {} bs'.format(amount, result))

if __name__ == '__main__':
	run()