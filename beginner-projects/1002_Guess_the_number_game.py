import random

def guessing(guess,answer,tries):
    if guess == answer and tries == 1 :
        print("CONGRATULATIONS!!!! YOU GUESSED THE NUMBER IN FRIST TRY")
        return True
    
    elif guess == answer:
        print(f"CONGRATULATIONS!!!! YOU GUESSED THE NUMBER IN {tries} try")
        return True
    elif guess != answer and tries == 3:
        print(f"Wrong answer, ALL TRIES OVER YOU LOSEEEEEEEE BOOOOOOOOOOOO\nThe answer was {answer}")
    elif guess != answer:
        if guess > answer:
            print("Wrong ANSWER, try guessing a smaller number")
            return False
        if guess < answer:
            print("Wrong ANSWER, try guessing a bigger number")
            return False
    
    
def bin_search(upper_limit):
    low = 1
    high = upper_limit

    while low <= high:
        mid = (low + high) // 2

        print(f"\nIs your number {mid}?")
        print("1. Higher")
        print("2. Lower")
        print("3. Correct")

        choice = input("Enter your choice: ")

        if choice == "1":
            low = mid + 1

        elif choice == "2":
            high = mid - 1

        elif choice == "3":
            print(f"I guessed your number! It was {mid}.")
            return

        else:
            print("Invalid choice.")

    print("Your answers were inconsistent.")
# print([x for x in range(0,1000)])

print("WELCOME TO PROFESSIONAL GUESSING GAME: ")
while True:
    print("\n1. Guess the number computer is thinking \n2. Imagine a number and let computer guess it")
    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            try:
                choice2 = int(input("1. Choose a random upper limit\n2. Choose upper limit yourself \nEnter your choice: "))
                tries = 1
                if choice2 == 1:
                    ul = random.randint(1,1000)
                    answer = random.randint(1,ul)
                    while tries < 4:
                        print("\nTHE COMPUTER IS THINKING OF A NUMBER, CAN YOU GUESS IT???")
                        guess = int(input("\nEnter your guess: "))
                        a = guessing(guess,answer,tries)
                        tries += 1
                
                elif choice2 == 2:
                    try:
                        ul = int(input("Enter an upper limit: "))
                        answer = random.randint(1,ul)
                        while tries < 4:
                            print("\nTHE COMPUTER IS THINKING OF A NUMBER, CAN YOU GUESS IT???")
                            guess = int(input("\nEnter your guess: "))
                            a = guessing(guess,answer,tries)
                            tries += 1
                    except ValueError:
                        print("Not a valid Upper Limit")
            except ValueError:
                print("Invalid CHOICE")
        
        elif choice == 2:
            ul = int(input("Enter the upper limit: "))
            print(f"Think of a number between 1 and {ul}.")
            bin_search(ul)


    except ValueError:
        print("Thats not a valid Choice")
                    
                    
                


        