'''
This is day 3, I think we're making a small game
'''
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("How old are you?"))
    if age <= 17:
        bill = 4
        print("Children pay $4")
    elif age <= 43:
        bill = 13
        print("Adults pay $13")
    else :
        bill = 19
        print("Seniors $19 please and thanks ")
    photo = input("Do you want a photo taken?")
    if photo == "y":
        print("This adds $3 dollars to the bill")
        if True:
            print(bill + 3)
        else :
            print(bill)
else :
    print("You're too short shorty!")
# number = int(input("Pick a number and I will tell you if it is odd or even "))
# if  number % 2 == 0:
#     print("That number is even")
# else :
#     print("That number is odd")
