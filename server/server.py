import asyncio
import websockets
import os

# This is a raw WebSocket server that TurboWarp expects
async def handler(websocket):
    print("TurboWarp connected!")
    try:
        async for message in websocket:
            print(f"Received: {message}")
            # Echo back to the client
            await websocket.send(message)
    except websockets.exceptions.ConnectionClosed:
        print("TurboWarp disconnected")

async def main():
    port = int(os.environ.get("PORT", 10000))
    async with websockets.serve(handler, "0.0.0.0", port):
        print(f"Server started on port {port}")
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())
