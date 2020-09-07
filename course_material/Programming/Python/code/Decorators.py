from typing import final, Final
from typing import Callable,TypeVar,Any,cast
T=TypeVar('T',bound=Callable[...,Any])

class BaseDecorated(object):
	def __init__(self):
		print("BaseDecorated: __init__()...")
		self.var1 : Final = 10

	@final
	def cannotoverride(self,var1 : int, var2: float) -> float:
		print("var1:",var1)
		print("var2:",var2)
		return var1*var2

	def funcdecorator(self,func,T)->T:
		def wrapper(*args,**keywords):
			print("funcdecorator(): Decorating function ",func," by a wrapper")
			return func(*args,**keywords)
		return cast(T, wrapper)
		

class DerivedDecorated(BaseDecorated):
	def __init__(self):
		print("DerivedDecorated: __init__()...")

	def cannotoverride(self,var1: int, var2: float) -> float:
		print("This line should not be printed...IDE or mypy TypeChecker must flag")	
		return var1*var2

def func1(n:int)->int:
	print("func1() invoked from decorator")
	return n

if __name__=="__main__":
	bd = BaseDecorated()
	bd.cannotoverride(1,100.0)
	bd.var1 = 1000
	print("bd.var1 (must be equal to 10 and flagged by TypeChecker):",bd.var1)
	dd = DerivedDecorated()
	dd.cannotoverride(1,100.0)
	decoratedfunc=dd.funcdecorator(func1,int)
	decoratedfunc(10)
