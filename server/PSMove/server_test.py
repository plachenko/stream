import asyncio
import websockets
import os
import sys
import time

import psmoveapi

class RedTrigger(psmoveapi.PSMoveAPI):
    def __init__(self):
        super().__init__()
        self.quit = False
        self.val = 0

    def on_connect(self, controller):
        controller.connection_time = time.time()
        print('Controller connected:', controller, controller.connection_time)

    def on_update(self, controller):
        # print(controller.buttons)
        # gyr = [controller.gyroscope.x, controller.gyroscope.y, controller.gyroscope.z]
        acc = [controller.accelerometer.x, controller.accelerometer.y, controller.accelerometer.z]
        if not controller.usb and controller.trigger:
            # self.val = 
            self.val = ", ".join(str(a) for a in acc)
            # self.val = ", ".join(str(a) for a in acc)
            # self.val = ". ".join([self.gyr, self.acc])
        # print('Update controller:', controller, int(time.time() - controller.connection_time))
        # print(controller.accelerometer, '->', controller.color, 'usb:', controller.usb, 'bt:', controller.bluetooth)
        up_pointing = min(1, max(0, 0.5 + 0.5 * controller.accelerometer.y))
        controller.color = psmoveapi.RGB(controller.trigger, up_pointing, 1 if controller.usb else 0.0)
        if controller.now_pressed(psmoveapi.Button.PS):
            self.quit = True
            asyncio.get_event_loop().stop()

    def on_disconnect(self, controller):
        print('Controller disconnected:', controller)

async def hello():
    uri = "ws://127.0.0.1:8080"
    async with websockets.connect(uri) as websocket:
        await websocket.send(api.val if api.val else "0")

api = RedTrigger()
while not api.quit:
    asyncio.run(hello())
    api.update()

asyncio.get_event_loop().run_forever()