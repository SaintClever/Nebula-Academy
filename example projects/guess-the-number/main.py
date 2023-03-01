from random import randint

rnum = randint(0, 50)
print("Guess a number between 0 and 50")
guessCount = 0
while True:
    guessCount += 1
    guess = int(input(": "))
    if guess > rnum:
        print(f"Lower! current attempt: {guessCount}")
    elif guess < rnum:
        print(f"Higher! current attempt:{guessCount}")
    else:
        (print(f"You win in {guessCount} guesses"), quit())