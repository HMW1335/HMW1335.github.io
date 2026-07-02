import json
import os
from fastapi import FastAPI, WebSocket
import uvicorn

app = FastAPI()

# This handles the HTTP health check automatically
@app.get("/health")
async def health():
    return {"status": "ok"}

# This handles the WebSocket connection
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    print("TurboWarp connected!")
    try:
        while True:
            data = await websocket.receive_text()
            message = json.loads(data)
            print(f"Received: {message}")
            await websocket.send_json({"status": "success"})
    except Exception as e:
        print(f"Connection closed: {e}")

if __name__ == "__main__":
    # Render requires a specific port
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)
