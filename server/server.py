import asyncio
import json
import os
import websockets

async def handler(websocket, path):
    # This handles actual WebSocket connections
    print("TurboWarp connected!")
    async for message in websocket:
        data = json.loads(message)
        # Your logic here
        await websocket.send(json.dumps({"status": "success"}))

async def health_check(path, request_headers):
    # This responds to Render's health check (HEAD/GET requests)
    if path == "/health":
        return websockets.http.response(200, [], b"OK")

async def main():
    port = int(os.environ.get("PORT", 10000))
    # 'process_request' allows us to intercept non-websocket requests
    async with websockets.serve(handler, "0.0.0.0", port, process_request=health_check):
        print(f"Server started on port {port}")
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
