import marshal
import shelve

class Example(object):
	def __init__(self):
		self.field1="field1"
		self.field2=[1,2,3,4,5,6,7,8,9,10]

	def print(self):
		print("field1:",self.field1)
		print("field2:",self.field2)


class Marshal(object):
	def __init__(self,serfile):
		self.serfile = serfile
		self.serializer = shelve.open(self.serfile,protocol=4,writeback=True)

	def marshal(self,objname,obj):
		print("Marshalling object:",objname)
		print("Shelve serializer:",list(self.serializer.items()))
		self.serializer[objname]=obj	
		#marshal.dump(obj,self.serializer)

	def unmarshal(self,objname):
		print("Unmarshalling object:",objname)
		print("Shelve serializer:",list(self.serializer.items()))
		value=self.serializer[objname]
		return value

	def sync(self):
		self.serializer.sync()

if __name__=="__main__":
	ex1=Example()
	marsh=Marshal("MarshalDB")
	marsh.marshal("array1",[1,2,3])
	deserialized=marsh.unmarshal("array1")
	print(deserialized)
	marsh.marshal("exampleobject1",ex1)
	deserialized_ex1=marsh.unmarshal("exampleobject1")
	deserialized_ex1.print()
	marsh.sync()
