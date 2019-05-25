import random

def roll(sides=6):
    num_rolled=random.randint(1,sides)
    return num_rolled

def main():
    user_input=""
    while(user_input.lower() != 'q'):
        print("Ready to roll ? ENTER=Roll. Q=Quit.")
        user_input = input()
        if (user_input.lower() != 'q'):
            num_rolled = roll(6)
            print("you rolled a",num_rolled)
        else:
            print("Thanks for playing dice game")
            break

main()