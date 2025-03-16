print("Guess a number between 1 and 10")
print("You will get 3 guesses")

guess_count = 0
guess_limit = 3
secret_number = 5

while guess_count < guess_limit:
    guess = input("Enter a guess: ")
    if not guess.isnumeric():
        print("You must enter an integer. Try again.")
    else:
        guess_count += 1
        if int(guess) == secret_number:
            print("You win!")
            break