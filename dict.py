# DICTIONARY: CAN STORE DATA IN KEY VALUE PAIR

#           : ORDERED
#           : NO DUPLICATE
#           : CHANGABLE
# SYNTAX:
#         KEY     VALUE
myInfo={ "name":"hansika",
         "email":"hansi@gamil",
         "mobile":"795623875",
         "age":24 }

print(myInfo)
print(myInfo["mobile"])


print(f"my name isis {myInfo["name"]}. and age {myInfo["age"]}. and email is {myInfo["email"]}. and number is {myInfo["mobile"]}")


#SYNTAX TO MODIFY THE DATA
for(value) in myInfo.values():
    print(value)
myInfo["name"]="nami"    
print(myInfo)

#SYNTAX TO UPDATA DATA
myInfo.update({"gender":"female"})
print(myInfo)



#SYNTAX TO DELETE DATA
del myInfo["email"]
myInfo.pop("age")
print(myInfo)