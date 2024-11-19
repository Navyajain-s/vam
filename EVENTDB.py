import mysql.connector
# create database connection to mysql
connection = mysql.connector.connect(host = "localhost", username = "root", password = "Aa9354788705bB", database = "event")
# to check if the connectiojn is established or not.
if connection.is_connected():
    print("Database is connected.")
else:
    print("Database is not connected.") 

# to create user table in databse
users = "create table if not exists addevent(eventname text, username text, eventdate text, email text, department text, mobile text)"
# to pass the cursor handle sql query.   
mycursor = connection.cursor()
# to execute the sql query
mycursor.execute(users)
connection.commit()
# to insert fname in users table
insertName = "insert into addevent values('{}','{}','{}','{}','{}','{}')".format(input("Enter Event Name: "),input("Enter User Name: "),input("Enter Event Date: "),input("Enter Email: "),input("Enter Department Name: "),input("Enter Mobile Number: "))
mycursor.execute(insertName)
connection.commit()
# to update the event details in database
# updateEvent = "update addevent set eventname = 'VAM' where department = 'BCA' "
# mycursor.execute(updateEvent)
# connection.commit()
# to delete the event from database
# deleteEvent = "delete from addevent where department = 'BCA'"
# mycursor.execute(deleteEvent)
# connection.commit()
# to fetch the event list from database
eventList ="select * from addevent" 
mycursor.execute(eventList)
print(mycursor.fetchall())
connection.commit()
# to drop the table
dropEvent = "drop table addevent"
mycursor.execute(dropEvent)
connection.commit() 