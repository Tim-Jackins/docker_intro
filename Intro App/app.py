from time import sleep

def sayHello():
	name = input("What's your name: ")
	print('Well how do you do', name)

if __name__=='__main__':
	while True:
		sayHello()
		sleep(.1)
