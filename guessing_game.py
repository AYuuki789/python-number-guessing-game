import random

random_number = random.randrange(1, 10)
tries = 5


while True:
    tries = 5
    ask_user = input("Do you want to play(y/n)").lower()
    if ask_user != "y":
        tries = 5
        break
    while tries > 0:
        
        
        try:
            guesss = int(input("Guess the random number(1,9): "))

            if guesss < 1 or guesss > 9:
             print("Out of range! Guess between 1 and 9.")
            
            
        except ValueError:
            print("invalid input please enter a number.")
            continue
        tries -= 1
        if guesss == random_number:
            print("Correctt! ")
            break

        elif guesss > random_number:
            print("Too high")

        else:
            print("Too low! ")

        print(f"Tries left: {tries}")


    if tries == 0:
        print("Game over! you ran out of tries! ")
                
    
    print("The correct number was:", random_number)


