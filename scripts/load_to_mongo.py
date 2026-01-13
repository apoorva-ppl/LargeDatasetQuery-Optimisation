from pymongo import MongoClient
import pandas as pd

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["youtube_data"]
collection = db["trending_videos"]

# Load cleaned dataset
df = pd.read_csv("../data/combined_youtube.csv")

# Insert data in batches
batch_size = 1000

for i in range(0, len(df), batch_size):
    batch = df.iloc[i:i+batch_size].to_dict("records")
    collection.insert_many(batch)

print(" Data inserted successfully")
