from pymongo import MongoClient

print("Connecting to MongoDB...")

client = MongoClient("mongodb://localhost:27017/")
db = client["youtube_data"]
collection = db["trending_videos"]

print("Connected successfully")

# Create indexes on frequently queried fields
collection.create_index("views")
collection.create_index("publish_time")
collection.create_index("channel_title")

print("✅ Indexes created successfully")


