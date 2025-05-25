from random import randint


conloop = "y"
guesses = 5

while conloop == "y":
    n = randint(0, 99)
    for taloop in range(guesses):
        print("Try", str(taloop+1), "/", guesses, ":")
        print("Guess the number! (0-99) ",)
        guess = int(input())
        if guess == n:
            print("Correct!")
            break
        elif guess > 99:
            print("Guess a number between 0 and 99!")
        else:
            if guess > n:
                horl = "Lower."
            else:
                horl = "Higher."
            if taloop == 4:
                print("Incorrect!")
            else:
                print("Incorrect! Try guessing", horl)
        print()
    print("The number was", n)
    conloop = input("\nTry again? (y/n)\n")

print("Thank you for playing!")
