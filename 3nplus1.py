def init():
	choice = int(input("Please enter an integer: "))
	conj(choice)


def conj(rc):
	count = 0
	while rc != 1:
		count = count + 1
		if rc % 2 == 0:
			rc = rc / 2
		else:
			rc = 3*rc + 1

	print(count)

	init()

init()