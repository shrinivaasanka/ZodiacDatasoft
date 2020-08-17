##############################################################################################################################################
# <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/">Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a>.
###############################################################################################################################################
# Course Authored By:
# -----------------------------------------------------------------------------------------------------------
# K.Srinivasan
# NeuronRain Documentation and Licensing: http://neuronrain-documentation.readthedocs.io/en/latest/
# Personal website(research): https://sites.google.com/site/kuja27/
# -----------------------------------------------------------------------------------------------------------
##############################################################################################################################################

import asyncio
import sys
from mavsdk import System

class DroneMAVSDKClient(asyncio.Protocol):
    def __init__(self, message, on_con_lost, clientloop):
        self.message = message
        self.on_con_lost = on_con_lost
        self.clientloop = clientloop

    def connection_made(self, transport):
        self.transport = transport
        self.transport.write(self.message.encode())
        print("connection_made(): message sent:", self.message)

    def data_received(self, data):
        peername = self.transport.get_extra_info('peername')
        print(peername, ":", data.decode())
        self.transport.close()

    def connection_lost(self, cl):
        print("Connection lost")

    async def drone_async_io(self,drone,mavsdkserverport,command):
        await drone.connect(system_address="udp://:"+str(mavsdkserverport))
        if command == "info":
            try:
                print("flight information:",await drone.info.get_flight_information())
                print("flight id:",await drone.info.get_identification())
                print("speed:",await drone.info.get_speed_factor())
                print("version:",await drone.info.get_version())
            except Exception as ex:
                print("Exception:",ex)
        if command == "arm": 
            try:
                await drone.action.arm()
            except Exception as ex:
                print("Exception:",ex)
        if command == "takeoff": 
            try:
                await drone.action.takeoff()
            except Exception as ex:
                print("Exception:",ex)
        if command == "goto_location":
            try:
                await drone.action.goto_location(78.0,7.0,100.0,0.0)
            except Exception as ex:
                print("Exception:",ex)
        if command == "camera":
            try:
                await drone.camera.start_video_streaming()
            except Exception as ex:
                print("Exception:",ex)

async def loop_print():
    cnt = 0
    while cnt < 10:
        print('loop_print()')
    cnt += 1
    return

async def main():
    clientloop = asyncio.get_running_loop()
    on_con_lost = clientloop.create_future()
    dronemavsdkclient = DroneMAVSDKClient(input(), on_con_lost, clientloop)
    transport, protocol = await clientloop.create_connection(lambda: dronemavsdkclient, 'localhost', 20000)
    drone = System()
    await dronemavsdkclient.drone_async_io(drone,14540,command="info")
    await dronemavsdkclient.drone_async_io(drone,14540,command="takeoff")
    await dronemavsdkclient.drone_async_io(drone,14540,command="arm")
    await dronemavsdkclient.drone_async_io(drone,14540,command="camera")
    await dronemavsdkclient.drone_async_io(drone,14540,command="goto_location")
    #await on_con_lost

if __name__ == "__main__":
    asyncio.run(main())
