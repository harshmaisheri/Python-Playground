from random import randint
# generate a number between [1 -10]
answer = randint(1, 10)

# input from user
# check the number is between 1 to 10
# check if number is right guess. Otherwise ask again


def guess_game(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print("Woahh!! You're a Genius")
            return True
        else:
            print("Woopsie! Try Again")
    else:
        print(f"Hey Bozo! I said 1 to 10")
        return False


if __name__ == "__main__":
    while True:
        try:
            guess = int(
                input(f"Guess a number from 1 to 10 : "))
            if guess_game(guess, answer):
                break

        except ValueError:
            print(
                f"Oops Like you didn't read it properly. Please enter a Number between 1 to 10")
            continue
