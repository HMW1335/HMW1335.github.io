import os
import json
import asyncio
import websockets
from pymongo import MongoClient

# Use the environment variable we will set in Render later
MONGO_URI = os.environ.get("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client.ihavenoidea  # This creates a database named 'ihavenoidea'
collection = db.test_data

async def handler(websocket):
    print("TurboWarp connected!")
    async for message in websocket:
        data = json.loads(message)
        # Placeholder: Save received message to MongoDB
        collection.insert_one({"message": data})
        print(f"Saved: {data}")
        await websocket.send(json.dumps({"status": "success"}))

async def main():
    # Render requires us to use the PORT environment variable
    port = int(os.environ.get("PORT", 10000))
    async with websockets.serve(handler, "0.0.0.0", port):
        print(f"Server started on port {port}")
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
