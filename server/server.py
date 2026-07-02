import socketio
import uvicorn

# Create a Socket.IO server
sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins='*')
app = socketio.ASGIApp(sio)

@sio.event
async def connect(sid, environ):
    print("TurboWarp connected!")

@sio.event
async def message(sid, data):
    print(f"Message received: {data}")
    # This broadcasts the message to everyone else connected instantly
    await sio.emit('message', data)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=10000)
