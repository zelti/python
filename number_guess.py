import random

def playAgain():
	again = str(input('¿Quieres volver a jugar?[s/n] =>'))
		
	if(again == 's'):
		run()
	elif(again == 'n'):
		return
	else:
		playAgain()


def needHelp(attempts, number, number_random):
	attempts += 1
	if(attempts >= 2):
		attempts = 0
		stg = 'menor' 
		if(number > number_random):
			stg = 'mayor'
		print('[tips]:....el número ingresado es "{}" al buscado'.format(stg))
	
	return attempts


def decoreMsg(msg):
	msgLen = len(msg)
	line = '-' * msgLen
	print('+-{}-+'.format(line))
	print('| {} |'.format(msg))
	print('+-{}-+'.format(line))


def run():
	decoreMsg('Adivina el número')
	number_found = False
	number_random = random.randint(0,20)
	attempts = 0
	while not number_found:
		number = int(input('Ingresa tu número => '))

		if(number == number_random):
			decoreMsg('Felicitaciones adivinaste el número')
			number_found = True
		else: 
			attempts = needHelp(attempts, number, number_random)

	playAgain()

if __name__ == '__main__':
	run()