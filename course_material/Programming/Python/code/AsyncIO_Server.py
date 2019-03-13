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

class ChatbotServer(asyncio.Protocol):
	def connection_made(self,transport):
		self.transport = transport

	def data_received(self, data):
		peername = self.transport.get_extra_info('peername')
		print(peername,":",data.decode())
		self.transport.close()

async def loop_print():
	cnt=0
	while cnt < 10:
		print('loop_print()')
	cnt += 1
	return 
	
async def main():
	serverloop=asyncio.get_running_loop()
	server = await serverloop.create_server(lambda: ChatbotServer(), 'localhost',10000)
	async with server:
		await server.serve_forever()

if __name__=="__main__":
	asyncio.run(main())


