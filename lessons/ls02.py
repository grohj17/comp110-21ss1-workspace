"""Simple guessing game."""

print("Guess a number!")

guess: int = int(input("Guess: "))

if guess == 8:
    print("correct")
else:
    if guess == 7:
        print("SO close, add 1!")
    else:
        if guess > 8:
            print("Lower!")
        else:
            if guess < 8:
                print("higher")
print("Game over")