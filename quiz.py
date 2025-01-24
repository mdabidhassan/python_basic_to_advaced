from operator import concat

print("welcome to my computer quiz")
playing=input("do you wanna play this game? ")
if playing !="yes":
  quit()
else:
    print("lets play game")
score=0
answer= input("What are cascading disasters?").lower()
if answer == "chain".lower():
    print("yo got 1 point")
    score += 1
else:
    print("incorrect")

answer=input("How does machine learning help in disaster management?").lower()
if answer == "prediction".lower():
    print("great work! you got 1 point")
    score += 1
else:
    print("incorrect")
answer = input(" What is the main role of coastal studies in disaster management?").lower()
if answer == "Mitigation".lower():
    print("you are doing great! you got 1 point")
    score += 1
else:
    print("incorrect")
    if score == 3:
        print("you achived total" + str(score) + "points!")
        print("highest achiver")
    elif score == 2:
        print("you achived total" + str(score) + "points!")
        print("poor marks!you have to do better! you got only" + str(score) + "points")
    else:
        print("you achived total" + str(score) + "points!")
        print("you are a backbencher")
