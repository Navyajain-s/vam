#function can perform
def printname():
    print("my name is")

    #function calling 
printname()



#argument function and parameter function 
def myage(age):
    print("my age is",age)


myage(23)

#area of square by function 
area= int(input("enter the side of square"))
def areasquare(a):
    return a*a
output=areasquare(area)
print("area of square is",output)



#delivery cost , food cost , price, discount , vat 
cost= int(input("enter the price of food"))
delivery= int(input("enter the delivery price of food"))
discount= int(input("enter the discount given on food"))
vat= int(input("enter the vat given on food"))
def price(cost,delivery,discount,vat):
    return cost+delivery-discount+vat
price=price(cost,delivery,discount,vat)
print("price of food is",price)