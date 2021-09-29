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
from geopy.geocoders import Nominatim
from Streaming_SetPartitionAnalytics import electronic_voting_machine
from collections import defaultdict
import random


class DroneMAVSDKClient(asyncio.Protocol):
    def __init__(self, message, on_con_lost, clientloop):
        self.message = message
        self.on_con_lost = on_con_lost
        self.clientloop = clientloop
        self.geolocator = Nominatim(user_agent="DroneEVM")
        self.voting_machine_dict = defaultdict(list)

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

    async def drone_async_io(self, drone, mavsdkserverport, command, address=None, candidates=None, idcontexts=None):
        await drone.connect(system_address="udp://:"+str(mavsdkserverport))
        print("drone_async_io(): Connected to MAVSDK server")
        async for state in drone.core.connection_state():
            print("state:", state)
            if state.is_connected:
                print(f"Drone discovered with UUID: {state.uuid}", state.uuid)
                break
        async for health in drone.telemetry.health():
            if health.is_global_position_ok:
                print("Global position estimate ok")
                break
        if command == "all":
            await drone.info.get_flight_information()
            await drone.action.arm()
            await drone.action.takeoff()
            await drone.camera.start_video_streaming()
            await drone.action.goto_location(78.0, 7.0, 100.0, 0.0)
            await drone.action.land()
        if command == "info":
            try:
                print("flight information:", await drone.info.get_flight_information())
                print("flight id:", await drone.info.get_identification())
                print("speed:", await drone.info.get_speed_factor())
                print("version:", await drone.info.get_version())
            except Exception as ex:
                print("Exception:", ex)
        if command == "arm":
            try:
                await drone.action.arm()
            except Exception as ex:
                print("Exception:", ex)
        if command == "takeoff":
            try:
                await drone.action.takeoff()
            except Exception as ex:
                print("Exception:", ex)
        if command == "goto_location":
            try:
                location = self.geolocator.geocode(address)
                print("location:", location.raw)
                await drone.action.goto_location(float(location.raw["lat"]), 1.0, float(location.raw["lon"]), 1.0)
                await drone.action.land()
            except Exception as ex:
                print("Exception:", ex)
        if command == "camera":
            try:
                await drone.camera.start_video_streaming()
            except Exception as ex:
                print("Exception:", ex)
        if command == "drone_EVM":
            try:
                if address != "fictitious":
                    location = self.geolocator.geocode(address)
                    print("location:", location.raw)
                    await drone.action.goto_location(float(location.raw["lat"]), 1.0, float(location.raw["lon"]), 1.0)
                else:
                    await drone.action.goto_location(78.0, 1.0, 70.0, 1.0)
                # await drone.action.land()
                await electronic_voting_machine_asynchronous(self.voting_machine_dict, idcontexts[0], candidates[int(random.random()*100) % len(candidates)], Streaming_Analytics_Bertrand=True)
            except Exception as ex:
                print("Exception:", ex)


async def electronic_voting_machine_asynchronous(voting_machine_dict, idcontexts, candidates, Streaming_Analytics_Bertrand=True):
    electronic_voting_machine(
        voting_machine_dict, idcontexts, candidates, Streaming_Analytics_Bertrand=True)


async def loop_print():
    cnt = 0
    while cnt < 10:
        print('loop_print()')
    cnt += 1
    return


async def main():
    clientloop = asyncio.get_running_loop()
    on_con_lost = clientloop.create_future()
    dronemavsdkclient = DroneMAVSDKClient(
        "DroneMAVSDKClient", on_con_lost, clientloop)
    transport, protocol = await clientloop.create_connection(lambda: dronemavsdkclient, 'localhost', 20000)
    drone = System()
    # await dronemavsdkclient.drone_async_io(drone, 14540, command="all")
    await dronemavsdkclient.drone_async_io(drone, 14540, command="info")
    await dronemavsdkclient.drone_async_io(drone, 14540, command="arm")
    await dronemavsdkclient.drone_async_io(drone, 14540, command="takeoff")
    # await dronemavsdkclient.drone_async_io(drone, 14540, command="camera")
    # await dronemavsdkclient.drone_async_io(drone, 14540, command="goto_location", address="175 5th Street NYC")
    candidates = ["NOTA", "CandidateA", "CandidateB"]
    idcontexts = ["/home/ksrinivasan/Krishna_iResearch_OpenSource_wc1/GitHub/asfer-github-code/python-src/testlogs/Streaming_SetPartitionAnalytics_EVM/PublicUniqueEVM_ID1.txt"]
    await dronemavsdkclient.drone_async_io(drone, 14540, command="drone_EVM", address="fictitious", candidates=candidates, idcontexts=idcontexts)
    # await on_con_lost

if __name__ == "__main__":
    asyncio.run(main())
