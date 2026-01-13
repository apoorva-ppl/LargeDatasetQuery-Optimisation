from pymongo import MongoClient

print("Connecting to MongoDB...")

client = MongoClient("mongodb://localhost:27017/")
collection = client.youtube_data.trending_videos

print("Connected successfully")
print("Total documents in collection:", collection.count_documents({}))

print("\nTop 5 most viewed videos:\n")

cursor = collection.find({}, {"title": 1, "views": 1, "_id": 0}) \
                   .sort("views", -1) \
                   .limit(5)

for video in cursor:
    print(video)

print("\nPagination example (page 2, 10 records):\n")

page = 2
limit = 10
skip = (page - 1) * limit

cursor = collection.find({}, {"title": 1, "_id": 0}).skip(skip).limit(limit)

for video in cursor:
    print(video)

print("\n✅ Query execution completed successfully")

