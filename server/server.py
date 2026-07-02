import asyncio
import json
import os
import websockets

async def handler(websocket):
    # This is ONLY for actual WebSocket connections
    print("TurboWarp connected!")
    try:
        async for message in websocket:
            data = json.loads(message)
            print(f"Received: {data}")
            await websocket.send(json.dumps({"status": "success"}))
    except Exception as e:
        print(f"Connection error: {e}")

async def health_check(path, request_headers):
    # This handles the HEAD/GET pings from Render
    if path == "/health":
        return websockets.http.response(200, [], b"OK")

async def main():
    port = int(os.environ.get("PORT", 10000))
    # We pass the health_check function to 'process_request'
    async with websockets.serve(handler, "0.0.0.0", port, process_request=health_check):
        print(f"Server started on port {port}")
        await asyncio.Future() 

if __name__ == "__main__":
    asyncio.run(main())
