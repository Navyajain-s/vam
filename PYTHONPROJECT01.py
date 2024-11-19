# Program to get a random six digit otp number.
import random
def generate_otp():
    otp = random.randint(100000,999999)
    return otp
otp = generate_otp()
print("Your OTP is:",otp)

# Program to convert dollar into rupees and vice versa.
def dollarintorupee(d):
    rupee = d * 84.03
    return rupee
def rupeeintodollar(r):
    dollar = r/84.03
    return dollar
dollar = float(input("Enter the amount(in dollars) you want to convert into rupee:"))
money = dollarintorupee(dollar)
print("The amount after conversion is :",money)
rupee = float(input("Enter the amount(in rupees) you want to convert into dollars:"))
money = rupeeintodollar(rupee)
print("The amount after conversion is :",money)






