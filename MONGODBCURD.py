from pymongo import MongoClient

# to create the mongodb client 
Client = MongoClient("mongodb://localhost:27017/")

# to create new database in client 
mydb = Client["ToDodb"]

# to create new connection(table) in database 
myCol = mydb["DailyTask"]

# # to insert the task in ToDo Database
# myTask = {"TaskName": input("Enter Task Name: "), "TaskDesc" : input("Enter Task Description: "), "TaskDate" : input("Enter Task Date: "), "TaskStatus" : 0}

# # to execute the insert in collection 
# myCol.insert_one(myTask)

# # to delete the task from the database 
# myDeleteTask = {"TaskDate":"11th Nov,2024"}

# # to pass the delete operation to collection 
# myCol.delete_one(myDeleteTask)

# creating a new collection(table) for event 
eventList = mydb["eventList"]

# # Add new event in event list
# event = [{"EventName" : "Talent Hunt", "EventDate" : "13th Nov 2024", "EventVenue" : "ITS College"},{"EventName" : "VAM fest", "EventDate" : "20th Nov 2024", "EventVenue" : "ITS College Class"}]

# # add event into event list 
# eventList.insert_many(event)
# # adding multiple items we need to put the dictionary into a list

# # to get the list of the event 
# allEvent = eventList.find()
# for event in allEvent:
#     print(event)

# # to update the event in the eventList collection 
# updateEvent = {"EventDate" :"14th Nov 2024"}
# eventList.update_one({"EventName" : "Talent Hunt"}, {"$set":updateEvent})
# updateEvent = {"EventDate" :"15th Nov 2024","EventVenue" : "ITS"}
# eventList.update_one({"EventName" : "Talent Hunt"}, {"$set":updateEvent})

updateEvent = {"EventDate": "16th Nov 2024"}
eventList.update_many({"EventVenue": "ITS"}, {"$set": updateEvent})


