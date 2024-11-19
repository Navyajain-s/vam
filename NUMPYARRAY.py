# Numpy :- It is used to work on large data set. 
# Its range is too large.It has High order function.
# It can reshape an arry.
# It can create N dimensional arrry.
# How to use Numpy in python:- to to the terminal and install pip install numpy.
import numpy as np
# Assign array in numpy
myData = np.array([1,2,3,4,5]) 
print(myData)
print(type(myData))
# Data Updation 
# myData[0]=11
# myData[1]=12
# myData[2]=13
# myData[3]=14
# myData[4]=15
# print("Array before Updation: ")
# print(myData)
# y = 11
# for i in range(0,5):
#     myData[i]=y
#     y=y+1
# print("Array after updation: ")
# print(myData)
# Accessing the values of the numpy array:
for i in range(0,5):
    print(myData[i])
myFriends=np.array(["Ivan","Anshu","Vani","Anjali"])
for name in myFriends:
    print(name)
i = 3
while i >= 0:
    print(myFriends[i]) 
    i=i-1
myFriends.sort()
print(myFriends)  



