##############################################################################################################################################
#<a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/">Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a>.
###############################################################################################################################################
#Course Authored By:
#-----------------------------------------------------------------------------------------------------------
#K.Srinivasan
#NeuronRain Documentation and Licensing: http://neuronrain-documentation.readthedocs.io/en/latest/
#Personal website(research): https://sites.google.com/site/kuja27/
#-----------------------------------------------------------------------------------------------------------
##############################################################################################################################################

import asyncio
import sys

class ChatbotClient(asyncio.Protocol):
	def __init__(self,message,on_con_lost,clientloop):
		self.message = message
		self.on_con_lost = on_con_lost
		self.clientloop = clientloop

	def connection_made(self,transport):
		self.transport = transport
		self.transport.write(self.message.encode())
		print("connection_made(): message sent:",self.message)

	def data_received(self, data):
		peername = self.transport.get_extra_info('peername')
		print(peername,":",data.decode())
		self.transport.close()

	def connection_lost(self,cl):
		print("Connection lost")

async def loop_print():
	cnt=0
	while cnt < 10:
		print('loop_print()')
	cnt += 1
	return 
	
async def main():
	clientloop=asyncio.get_running_loop()
	on_con_lost=clientloop.create_future()
	transport,protocol = await clientloop.create_connection(lambda: ChatbotClient(input(),on_con_lost,clientloop), 'localhost',10000)
	#await on_con_lost

if __name__=="__main__":
	asyncio.run(main())


