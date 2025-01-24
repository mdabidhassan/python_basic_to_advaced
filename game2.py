answer = input(" What is the main role of coastal studies in disaster management?").lower()
if answer != "Mitigation".lower():
    print("you are doing great! you got 1 point")
    score += 1
else:
    print("incorrect")
    print("your total score is" + int(score))
if score == 3:
    print("you achived total" + int(score) + "points!")
    print("highest achiver")
elif score == 2:
    print("poor marks!you have to do better! you got only" + int(score) + "points")
else:
    print("you are a backbencher")
