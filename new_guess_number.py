import random


range_in = input("Create a range: ")

if range_in.isdigit():
    range_in = int(range_in)
    if range_in <= 0:
        print("input valid number")
        quit()
else:
    print("wrong numbr")
    quit()
random_number = random.randint(0,range_in)
score=0
while True:
    score+=1
    user_input = input("guess number")
    if user_input.isdigit():
       user_input = int(user_input)
       if user_input <= 0:
            print("input valid number")
            quit()
    if user_input==random_number:
        print("you are in track")
        print("you find the answer after",score,"times leter")
        break
    else:
        print("wrong")
        continue