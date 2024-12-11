from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["medisearch"]
collection = db["medicines"]

# Insert sample medicine data
medicine_data = [
    {
        "name": "paracetamol",
        "description": {
            "usage": "Used to treat pain and inflammation.",
            "why_to_use": "Effective for reducing fever and relieving pain.",
            "advantages": "Fast-acting, over-the-counter availability.",
            "disadvantages": "Can cause stomach upset if taken on an empty stomach.",
            "side_effects": "Nausea, dizziness, allergic reactions."
        }
    }
]

# Insert the data into the collection
collection.insert_many(medicine_data)
print("Sample data inserted successfully.")
