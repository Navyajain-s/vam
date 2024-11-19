# try block : 
#     error  
# catch block : 
#     type of error 
# print(x) [name error] 
# try:
#     print(x)
# except NameError:
#      print("x not defined")
# try:
#     y = 1/0 #ZeroDivisionError
#     print(y)
# except ZeroDivisionError:
#     print("Dividing by zero gives zero divion error")
# try:
#     a = "Deepanshu Anand"
#     b = int(a)
#     print(b)
# except ValueError:
# #     print("String cannot be typecasted as Int") 
# import os
# try:
#    os.remove("myfile.txt")
# except FileNotFoundError:
#     print("The file to be deleted is not found.") 
# myList = ["Deepanshu","Harsh","Nikhil"]   
# try:
#     print(myList[4])
# except IndexError:
#    print("4th index value is out of range")    
# try:
#     x = 5
#     if x > 5:
#     print(x)
#     else:
#     print(x)
# except IndentationError:
#     print("The indentation is wrong")
# This type of error is suppose to be handled manually.
# x = "Deepanshu"
# y = 4
# try:
#     c = x + y
#     print(c)
# except TypeError:
#     print("String cannot be concatenated to integer")
# using finally statement
# executed either error is found or not
try:
    print(x)
except NameError:
     print("x not defined")
finally:
     print("The x is to be printed anyways.")
          

