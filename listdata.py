#data storage in ,list ,tupple ,stack ,distionary 

#list is used too store multiple data 
#list store diff types of data like string,int , float 
#it can contain dublicate data 

# friendname=["mohan","rohan","rahul"]
#to get access single data from list 
# print(friendname[0])   
# print(friendname[2])

#want to print complete list
 #print(friendname)
# for name in friendname:
#     print(name) 

# friend=["navya","mohit","rahul",23,43,56]
# for name in friend:
#  print(name)

#operation in list 




#apppend adds new variable in list at end only takes on arg

# friend.append("priya")
# friend.append("preet")
# for name in friend:
#  print(name)



#insert will add new variable in list at any position
#if position value is high entered compiler automatically enter that at last
# friend.insert(12,"pooja")
# for name in friend:
#   print(name) 



#to remove data from list  
#only remove data will remove from value nt by index
#only one at a time can remove data

# friend.remove("pooja")
# for name in friend:
#   print(name)




#pop will remove data from list by index
# friend.pop( 1)
# for name in friend:
#   print(name)


#to reverse the list 
# friend.reverse()
# for name in friend:
#   print(name)  


#clear all list 
# friend.clear()
# for name in friend:
#   print(name)


#printing data in a range slicing
# friend.append("hello")
# for name in friend[1:3]:
#   print(name)

# for name in friend[2:8]:
#   print(name)
  

#neg slicing
# print(friend)
# for name in friend[-3:-1]:
#   print(name)


# for name in friend[:-1]:
#   print(name)  

# for name in friend[-8:]:
#   print(name)    



#sorting the name 
# we cant sort list if it has string and int both data type
# friend.sort()
# for name in friend:          #ERRORR 
#   print(name)                  #ERRORR 


friend=["navya","mohit","rahul","hello","cutie"]
# friend.sort()
# for name in friend:
#     print(name)


friend[0]="priya"
friend.sort()
for name in friend:
    print(name)