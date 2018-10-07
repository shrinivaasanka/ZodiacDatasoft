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

class Reflect:
	def __init__(self):
		self.attr1="attr1"

	def function1(self,a,b):
		qr=divmod(a,b)
		print("This is function1()")
		print("function1() : division ",a,"%",b,"; quotient = ",qr[0],"; remainder = ",qr[1])

	@classmethod
	def function2(cls,c):
		print("This is classmethod function2():",c)
		print("cls: ",cls)

class ReflectDerived(Reflect):
	def function3():
		print("This is function3()")
	
if __name__=="__main__":
	rdiv=Reflect()
	rdivder=ReflectDerived()
	rdiv.function1(10,3)
	print("classmethod invoked on instance:")
	rdiv.function2(10)
	print("classmethod invoked on class:")
	Reflect.function2(10)
	print("classmethod invoked on derived class:")
	ReflectDerived.function2(10)
	print(dir(rdiv.function1.__func__))
	rdiv.function1.__func__.whoami="This is function1"
	print("__func__.whoami = ",rdiv.function1.__func__.whoami)
	print("func_code = ",rdiv.function1.func_code)
	print("func_closure = ",rdiv.function1.func_closure)
	print("func_dict = ",rdiv.function1.func_dict)
	print("func_globals = ",rdiv.function1.func_globals)
