from pymongo import MongoClient

# Sample sensor data
sensor_1 = {"id": "0001", "name": "Temp", "location": "Room10", "value": "22"}
sensor_2 = {"id": "0002", "name": "Temp", "value": "22"}

# Connect to MongoDB (assuming it's running locally on default port 27017)
db_client = MongoClient('mongodb://localhost:27017/')

# Access or create a database
db = db_client['details']  # Use 'details' as the database name

# Access or create a collection within the database
storage = db['storage']

# Insert data into the collection
result_1 = storage.insert_one(sensor_1)
result_2 = storage.insert_one(sensor_2)

# Print the inserted document IDs
print(f"Inserted document IDs: {result_1.inserted_id}, {result_2.inserted_id}")

# Query for a specific document with id '0001'
query = {"id": "0001"}
sensor_data = storage.find_one(query)

# Print the retrieved document
if sensor_data:
    print(f"Found document: {sensor_data}")
else:
    print("Document not found")

# Close the MongoDB connection
db_client.close()
