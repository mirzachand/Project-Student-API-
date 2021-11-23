from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/', 27017)
print(client.list_database_names())

db = client['Netzwerk']

# Student Details

collection = db['steve']
#steve details
stevedetails ={"_id": 1, "Course": "FSD & Python", "Tutor":"karthikeya-(FSD) & robert-(Python)", "Timing":"FSD-(10.00AM-11.00AM) & Python-(11.00AM-12.00PM)"}
collection.insert_one(stevedetails)
print(collection.find_one(stevedetails))

collection = db['mirza']
#mirza details
mirzadetails ={"_id": 2, "Course": "SD", "Tutor":"HarrysonWells", "Timing":"1.00PM-2.00PM"}
collection.insert_one(mirzadetails)
print(collection.find_one(mirzadetails))

collection = db['Allen']
#Allen details
Allendetails ={"_id": 3, "Course": "Python", "Tutor":"karthikeya", "Timing":"11.00AM-12.00PM"}
collection.insert_one(Allendetails)
print(collection.find_one(Allendetails))



# Tutor Details

collection = db['karthikeya']
#karthikeya details
karthikeyadetails ={"_id": 4, "Course": "FSD & Python", "Student":"steve-(FSD) & Allen-(Python)", "Timing":"FSD-(10.00AM-11.00AM) & Python-(11.00AM-12.00PM)"}
collection.insert_one(karthikeyadetails)
print(collection.find_one(karthikeyadetails))

collection = db['robert']
#robert details
robertdetails ={"_id": 5, "Course": "Python", "Student":"steve", "Timing":"11.00AM-12.00PM"}
collection.insert_one(robertdetails)
print(collection.find_one(robertdetails))

collection = db['HarrysonWells']
#HarrysonWells details
HarrysonWellsdetails ={"_id": 6, "Course": "SD", "Student":"Mirza", "Timing":"1.00PM-2.00PM"}
collection.insert_one(HarrysonWellsdetails)
print(collection.find_one(HarrysonWellsdetails))




