# NUMBER GUESSING GAME
num = 5 # this is the number to be guessed
print("Welcome to the number guessing game!")
print("You have 5 chances to guess the number between 1 and 10.")
guess = int(input("write a number that you guess: "))
for i in range(4):
    if guess == num:
        print(f"your guess is correct, the number is {num}")
        break
    else:
        guess = int(input("Try again, write a number that you guess: "))
else:
    print(f"you tried 5 times, the number is {num}")
    print("GAME OVER")