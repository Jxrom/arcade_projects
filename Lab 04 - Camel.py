import random

def main():
    MILES_TRAVELLED = 0
    THIRST = 0
    CAMEL_TIREDNESS = 0
    NATIVE_DISTANCE = -20
    CANTEEN_DRINKS = 3

    print("Welcome to Camel!")
    print("You have stolen a camel to make your across the great Mobi desert.")
    print("The natives want their camel back and are chasing you down! Survive your")
    print("desert trek and out run the natives.")

    done = False

    while done == False:
        print("===============================")
        print("+ A. Drink from your canteen. +")
        print("+ B. Ahead moderate speed.    +")
        print("+ C. Ahead full speed.        +")
        print("+ D. Stop for the night.      +")
        print("+ E. Status check.            +")
        print("+ Q. Quit.                    +")
        print("===============================")

        user_choice = input("What is your choice? ")

        if user_choice.upper() == "Q":
            print("You quitted the game!")
            break
        elif user_choice.upper() == "E":
            print("Miles traveled: ", MILES_TRAVELLED)
            print("Drinks in canteen: ", CANTEEN_DRINKS)
            print("The natives are {} miles behind you.".format(MILES_TRAVELLED - NATIVE_DISTANCE))
        
        elif user_choice.upper() == "D":
            print("You stop for the night.")
            print("Your camel is happy.")

            CAMEL_TIREDNESS = 0
            NATIVE_DISTANCE += random.randrange(7, 14)

        elif user_choice.upper() == "C":
            full_miles_val = random.randrange(10, 21)
            CAMEL_TIREDNESS += random.randrange(1, 3)
            NATIVE_DISTANCE += random.randrange(7, 14)
            THIRST += 1
            
            MILES_TRAVELLED += full_miles_val
            print("You travelled {}".format(full_miles_val))

        elif user_choice.upper() == "B":
            mod_miles_val = random.randrange(5, 12)
            NATIVE_DISTANCE += random.randrange(7, 14)
            CAMEL_TIREDNESS += 1
            
            MILES_TRAVELLED += mod_miles_val
            print("You travelled {}".format(mod_miles_val))

        elif user_choice.upper() == "A":

main()
