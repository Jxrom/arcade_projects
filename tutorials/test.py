import random

# Random number range from 1-49
my_number = random.randrange(50)

# Random number range from 100-200
my_number2 = random.randrange(100, 201)

print(my_number)
print(my_number2)

# 25% change of meeting the dragon
for i in range(20):
    if random.randrange(5) == 0:
        print("DRAGON!!!")
    else:
        print("No Dragon. :(")
