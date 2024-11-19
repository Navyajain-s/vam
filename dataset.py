#create list,tuple,set,dict
#add data pawan,manan,tanya ,mukul
#delete pawan 
#access all data
#update mukul to mukul sharma 
#add manan and print the data 


#all work in list 
# friendname=["pawan","man","anya" ,"kul"]
# friendname.append("mukul")
# friendname.append("tanya")
# for name in friendname:
#     print(name)


# #remove pawan    
# friendname.remove("pawan")
# for name in friendname:
#      print(name)

# #print all list    
# for name in friendname:
#      print(name) 

# #update mukul to mukul sharma
# friendname[3]="mukul sharma"
# for name in friendname:   
#      print(name)  


#all data in tuple
# mytuple=("pawan","man","anya" ,"kul")

# mytuplelist=list(mytuple)
# mytuplelist[3]="mukul sharma"
# for name in mytuplelist:
#  print(name)
# mytuplelist.append("manan")
# for name in mytuplelist:
#  print(name)
# mytuplelist.remove("pawan")
# for name in mytuplelist:
#  print(name)


#all data in set
# myset={"pawan","man","anya" ,"kul"}
# myset.add("mukul sharma")
# for name in myset:
#  print(name)
# myset.remove("pawan")
# for name in myset:
#  print(name)
#  set cant modify 


#all data in dict

mydict={"name":"pawan","age":20 ,"gender": "female"}
print(mydict)
mydict.update({"gender":"male"})
mydict.update({"email":"p@gmail.com"})

print(mydict)

del mydict["name"]
mydict.pop("age")
print(mydict)
