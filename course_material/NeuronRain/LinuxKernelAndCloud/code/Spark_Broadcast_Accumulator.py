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
from pyspark.sql import SQLContext, Row 
import operator
import sys
import json
import threading
from pyspark.accumulators import AccumulatorParam

broadcast_var="0"
accumulator_var=0

class VectorAccumulatorParam(AccumulatorParam):
     def zero(self, value):
         return [0.0] * len(value)
     def addInPlace(self, val1, val2):
         for i in range(len(val1)):
              val1[i] += val2[i]
         return val1

def broadcast_accumulator_receiver(x):
	global broadcast_var
	global accumulator_var
	print "broadcast_accumulator_receiver():broadcast_var=",broadcast_var.value
	print "broadcast_accumulator_receiver():accumulator_var=",accumulator_var

def SparkBroadcastAccumulator(n): 
	global broadcast_var
	global accumulator_var
	spcon = SparkContext("local[2]","SparkBroadcastAccumulator")
	broadcast_var=spcon.broadcast("broadcast_message")
	accumulator_var=spcon.accumulator(0)
	spcon.parallelize(xrange(1,n)).foreach(lambda x: broadcast_accumulator_receiver(accumulator_var.add(x)))

if __name__=="__main__":
	SparkBroadcastAccumulator(100)

