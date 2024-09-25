#for loop is used to complete the iteration or repeating the task 
name=input("enter your name")
#eg in c for(int i=0;i<10;i++)
for i in name:
    print(i)

    #print the no 1 to 10 

for x in range(1,11):
     print(x)

    #print odd no 

for y  in range(1,11):   
  if y %2!=0:
      print(y)

      #using stepsize  
for z in range(1,11,2):  #2 states herre te step size 
    print(z)


  #print odd and even no using for loop  

for a in range(1,21):
    if a%2==0:
        print("even no",a)
    else:
        print("odd no",a)