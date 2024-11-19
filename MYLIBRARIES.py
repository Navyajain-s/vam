# Numpy :- data set creation 
# Pandas :- data set represent
# Matplotlib :- graphically data representation 
import numpy as np
import pandas as pd
import  matplotlib.pyplot as plt
# years = np.array([2020,2022,2023])
# grade = np.array([81,83,73])
# plt.plot(years,grade,marker='o') #for creating a graph with marker. 
# plt.title("MY ACADEMIC PERFORMANCE") #for giving a title. 
# plt.xlabel("Years........")#for naming x axis. 
# plt.ylabel("Grades.......")#for naming y axis. 
# plt.grid()#for a grid.
# plt.show()#for showing a graph.
# x = np.array([90,75,80,65,50,70,50,65,57])

# plt.pie(x)
# plt.title("...PIE CHART...")
# name = np.array(["Python","Java","React","C++","C","C#","R","CSS","RUBY"])
# plt.legend(name) #for showing the titles.
# plt.show()
# Creation a bar graph 
# plt.bar(years,grade)
# creating a scatter graph 
# plt.scatter(years,grade)
# plt.show()
# x = np.array([1,7,8,11,9,3,2,4])
# find the mean, min, max  and sort the array.
# print(x.mean())
# print(x.min())
# print(x.max())
# sorting the array
# x.sort()
# print(x)
# without using high order function/sort
# array slicing 
# for i in x:
#     print(i)
# print(x[-6:-2:]) # blanck = 0
# shape , reshape 
# print(x.shape)
# mydata = x.reshape(2,4)
# print(mydata.shape)
# print(mydata)
# y=np.array([3,1,7,9,2,11,8,10])
# adding two arrays 
# print(x+y)
# x = np.array([1,2,3,4])
# mydataframe = pd.DataFrame(x)
# pandas will represent your large data set.
# print(mydataframe)
# mydata = pd.DataFrame(data = np.arange(0,100).reshape(10,10))
# print(mydata)
# print(mydata.head()) #print the top five rows default value hai 
# print(mydata.tail()) #print last five rows 
#for specific value
# print(mydata.head(3))
empsalary = pd.DataFrame(data = np.arange(0,100).reshape(10,10))
# adding 100 rs bonus in all 
# print(empsalary + 1000)
# all info is gathered.
# print(empsalary.describe())
# print(empsalary.mean())
# print(empsalary.mode())
# print(empsalary.median())
print(empsalary.loc[[0,3]]) # print data in number of rows.
print(empsalary.loc[[9,]]) #prints the data of last row 
print(empsalary.loc[[0,]])
