'''
This is day two for the course
'''
#Lesson 2
# print(len("12345"))
# print(type("Xavier"))
# print(type(23))
# print(type(23.4))
# print(type(True))
# print(int("123"))
# print("Number of letters in your name: " + str(len(input("Enter your name "))))
print("Welcome to the tip calculator!")
total = float(input("What was the total bill? $ "))
tip_choice = float(input("How much would you like to tip? 10, 15, or 20 $ "))
total_with_tip = float((tip_choice / 100) * total + total)
people_split = float(input("How many people want to split the bill? "))
total_bill = total_with_tip / people_split
print(f"Your total bill after splitting is : ${total_bill:.2f}")
