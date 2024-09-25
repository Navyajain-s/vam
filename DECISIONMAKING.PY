# First Age Check
age = int(input("enter your age: "))
if age > 18:
    print("you are eligible for vote")
else:
    print("you are not eligible for vote")

# Enhanced Voting Eligibility Check
myage = int(input("enter your age: "))
if myage > 18 and myage < 60:
    print("you are eligible for vote")
elif myage > 60:
    print("you are eligible for supervote")
else:
    print("you are not eligible for vote")
