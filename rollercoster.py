print("Welcome to rollercoster :) ")
height = int(input("ENter yoour Height "))
bill = 0
if height <= 120:
    print("You can ride the roler :) ")
    age = int(input("what's your Age ?"))
    if age > 18:
        bill = 8
        print("pay $8 ")
    else:
        bill = 4
        print("pay $4 ")

    want_photo = input("Do u want photo on if yes/no y or n ")
    if want_photo == "y":
        bill += 3
        print(f"ur final bill is {bill}")
else:
    print("You can't ride roller :( ")
