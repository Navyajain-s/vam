#create file with name and ext 

myFile= open("navya.txt","w")
           

#writing data into file
myFile.write("hello")

#closing the file
myFile.close()


#read data from file
readFile= open("navya.txt","r")
print(readFile.read())


#detete file
# import os 
# os.remove("navya.txt")

#create stock api in json ~~~~ java script obj notation
#jsno file contatin data in keyvalue pair and in brackets it is always said as obj 
#curly barces json obj {}
#square braces jsonarray []
mystock=open("my stock.json","w")
mystock.write("{'name':'navya'}")

#read and write data in excel ,csv,txt nd json 