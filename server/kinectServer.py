import freenect
import cv2
import frame_convert2
import base64
import numpy as np
import asyncio
import websockets

cam = 0

def get_depth():
    data = frame_convert2.pretty_depth_cv(freenect.sync_get_depth()[0])
    #data = data.astype(np.unint8)
    img = cv2.imencode('.JPEG', data)[1].tostring()
    enData = base64.b64encode(img).decode('UTF-8')
    return enData

def get_video(c):
    global cam
    data = frame_convert2.video_cv(freenect.sync_get_video(c)[0])
    #data,_ = freenect.sync_get_video()
    #data = cv2.cvtColor(data, cv2.COLOR_RGB2BGR)
    img = cv2.imencode('.JPEG', data)[1].tostring()
    enData = base64.b64encode(img).decode('UTF-8')
    return enData

async def get_cam():
    global cam
    #camD = await websocket.recv()
    #cam = int(camD)

async def show_cam():
    await websocket.send(get_video())

async def server(websocket, path):
    global cam
    while True:
        await websocket.send(get_video(0))

# start_server = websockets.serve(server, "192.168.0.62", 9000)
start_server = websockets.serve(server, "0.0.0.0", 9000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()