##############################################################################################################################################
#<a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/">Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a>.
##############################################################################################################################################
#Course Authored By:
#-----------------------------------------------------------------------------------------------------------
#K.Srinivasan
#NeuronRain Documentation and Licensing: http://neuronrain-documentation.readthedocs.io/en/latest/
#Personal website(research): https://sites.google.com/site/kuja27/
#-----------------------------------------------------------------------------------------------------------

from pyspark import SparkContext, SparkConf

def Map(n):
	return (1,[n])

def Reduce(n1,n2):
	print "n1:",n1
	print "n2:",n2
	if n1 is None:
		return n2
	if n2 is None:
		return n1
	if n1[len(n1)-1] < n2[1]:
		print "Reduce:",n1+n2
		return n1 + n2
	if n2[len(n2)-1] >= n1[1]:
		print "Reduce:",n2+n1
		return n2 + n1
	if n1[len(n1)-1] >= n2[1]:
		print "Reduce:",n1+n2
		return n1 + n2
	if n2[len(n2)-1] < n1[1]:
		print "Reduce:",n2+n1
		return n2 + n1

def sorted(integers):
	prev=integers[0]
	for x in integers[1:]:
		if x > prev:
			return False
		prev=x
	return True

def MapReduce(integers):
	spcon = SparkContext("local[10]","Spark_MapReduce")
	while not sorted(integers):
		integerstuple=spcon.parallelize(integers).map(Map).reduce(Reduce)
		integers=[]
		for n in integerstuple:
			if type(n) == list:
				integers.append(n[0])
		print "Bitonic Sequence of Integers:"
		print integers

if __name__=="__main__":
	integers=[3,2,4,5,23,6,7,12,32,15,16]
	MapReduce(integers)	

