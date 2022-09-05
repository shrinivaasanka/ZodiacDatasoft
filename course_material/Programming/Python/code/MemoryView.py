##############################################################################################################################################
# <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/">Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a>.
###############################################################################################################################################
# Course Authored By:
# -----------------------------------------------------------------------------------------------------------
##############################################################################################################################################
# K.Srinivasan
# NeuronRain Documentation and Licensing: http://neuronrain-documentation.readthedocs.io/en/latest/
# Personal website(research): https://acadpdrafts.readthedocs.io
##############################################################################################################################################

def memview(object,datatype):
	mv = memoryview(object)
	print(datatype," - Memory view:",mv.tolist())

if __name__=="__main__":
	x=b"20390293091sdlklsd"
	y=90229
	z=2910290.234
	memview(x,type(x))
	memview(y.to_bytes(y.bit_length(),byteorder="little"),type(y))
	memview(y.to_bytes(y.bit_length(),byteorder="big"),type(y))
	memview(float.hex(z).encode(),type(z))
