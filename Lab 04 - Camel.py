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
        print()
        print("===============================")
        print("+ A. Drink from your canteen. +")
        print("+ B. Ahead moderate speed.    +")
        print("+ C. Ahead full speed.        +")
        print("+ D. Stop for the night.      +")
        print("+ E. Status check.            +")
        print("+ Q. Quit.                    +")
        print("===============================")

        print()
        user_choice = input("What is your choice? ")
        print()

        # QUIT
        if user_choice.upper() == "Q":
            print("You quitted the game!")
            break

        # STATUS CHECK
        elif user_choice.upper() == "E":
            print("Miles traveled: ", MILES_TRAVELLED)
            print("Drinks in canteen: ", CANTEEN_DRINKS)
            print("The natives are {} miles behind you.".format(
                MILES_TRAVELLED - NATIVE_DISTANCE))

        # STOP FOR THE NIGHT
        elif user_choice.upper() == "D":
            print("You stop for the night.")
            print("Your camel is happy.")

            CAMEL_TIREDNESS = 0
            NATIVE_DISTANCE += random.randrange(7, 14)

        # AHEAD FULL SPEED
        elif user_choice.upper() == "C":
            full_miles_val = random.randrange(10, 21)
            MILES_TRAVELLED += full_miles_val
            THIRST += 1

            CAMEL_TIREDNESS += random.randrange(1, 4)
            NATIVE_DISTANCE += random.randrange(7, 15)
            OASIS = random.randrange(20)

            if OASIS == 10:
                THIRST = 0
                CAMEL_TIREDNESS = 0
                CANTEEN_DRINKS = 3

                print("You happened to be in oasis!")
                print("Canteen filled, thirst replenished, camel is well rested.")
            else:
                print("You travelled {} miles.".format(full_miles_val))

        # AHEAD MODERATE SPEED
        elif user_choice.upper() == "B":
            mod_miles_val = random.randrange(5, 13)
            MILES_TRAVELLED += mod_miles_val
            THIRST += 1

            NATIVE_DISTANCE += random.randrange(7, 15)
            CAMEL_TIREDNESS += 1
            OASIS = random.randrange(20)

            if OASIS == 10:
                THIRST = 0
                CAMEL_TIREDNESS = 0
                CANTEEN_DRINKS = 3

                print("You happened to be in oasis!")
                print("Canteen filled, thirst replenished, camel is well rested.")
            else:
                print("You travelled {} miles.".format(mod_miles_val))

        # CANTEEN DRINK
        elif user_choice.upper() == "A":
            if CANTEEN_DRINKS != 0:
                CANTEEN_DRINKS -= 1
                THIRST = 0
                print("You take a drink.")
            else:
                print("Canteen Drinks is Empty! Lunatic")

        # THIRST
        if THIRST > 6:
            print("You died of thirst.")
            print("<==== GAME OVER ====>")
            done = True
        elif THIRST > 4:
            print("You are thirsty.")

        # CAMEL TIREDNESS
        if CAMEL_TIREDNESS > 8:
            print("Your camel is dead.")
            print("<==== GAME OVER ====>")
            done = True
        elif CAMEL_TIREDNESS > 5:
            print("Your camel is getting tired.")

        # NATIVE DISTANCE FROM YOU
        if MILES_TRAVELLED - NATIVE_DISTANCE <= 0:
            print("The natives have caught up with you!")
            print("<==== GAME OVER ====>")
            done = True
        elif MILES_TRAVELLED - NATIVE_DISTANCE < 15:
            print("The natives are getting close!")

        # WIN CHECK
        if MILES_TRAVELLED >= 200:
            print()
            print("Congratulations!!!")
            print("You have crossed the entire dessert!")
            done = True


main()
