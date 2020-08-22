from random import randint
num=randint(1,9)
guess=-1
print("Guess the number between 1 & 10:")
while guess!=num:
	guess=int(input("Guess the Number:"))
	if guess!=num:
		print("OOPS,Wrong guess")

	else:
		print("Congratulations,the number you guessed is correct")
