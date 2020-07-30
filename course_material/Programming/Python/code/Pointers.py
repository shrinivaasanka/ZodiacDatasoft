##############################################################################################################################################
#<a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/">Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a>.
###############################################################################################################################################
#Course Authored By:
#-----------------------------------------------------------------------------------------------------------
##############################################################################################################################################
#K.Srinivasan
#NeuronRain Documentation and Licensing: http://neuronrain-documentation.readthedocs.io/en/latest/
#Personal website(research): https://sites.google.com/site/kuja27/
##############################################################################################################################################

from ctypes import *

def simulate_pointers():
	sentence1 = "This is a sentence"
	try:
		print("Immutable - sentence1:",sentence1)
		sentence1[2] = 'a'
	except Exception as ex:
		print("Exception:",ex)
		sentence1_ptr = c_wchar_p(sentence1)
		#sentence_ptr = pointer(sentence)
		print("Pointer to sentence1 string:",sentence1_ptr)
		sentence1_ptr.value = 'This is different sentence'
		print("Changed pointer copy of sentence1:",sentence1_ptr.value)
		sentence2 = create_string_buffer(10)
		print("sentence2 - RAM contents after create_string_buffer():",sentence2.raw)
		integer1 = 100
		integer1_ptr = c_void_p(integer1)
		integer1_ptr.value = 200
		print("Pointer to integer1:",integer1_ptr)
		print("immutable - integer1:",integer1)
		print("Changed pointer copy of integer1:",integer1_ptr.value)
		
	
if __name__=="__main__":
	simulate_pointers()	
