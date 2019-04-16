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
from pyspark.ml.fpm import FPGrowth
from sympy.combinatorics.partitions import Partition
from sympy.functions.combinatorial.numbers import nT
spcon = SparkContext("local[2]","Spark_FPGrowth_SurvivalIndexTimeout")

def processes_set_partitions(processes):
	number_of_partitions=nT(len(processes))
	processes_partitions=Partition(processes)
	for p in spcon.range(number_of_partitions).collect():
		print "======================================================="
		print "Partition:",processes_partitions + p
		print "Partition Rank:",(processes_partitions + p).rank

def SurvivalIndexTimeout(timeoutpidsmap):
	global spcon
	sqlcon = SQLContext(spcon)
	timeoutdf=sqlcon.createDataFrame(timeoutpidsmap,['index','process_ids'])
	fpGrowth=FPGrowth(itemsCol="process_ids",minSupport=0.5,minConfidence=0.5)
	fpModel=fpGrowth.fit(timeoutdf)
	fpModel.freqItemsets.show()
	fpModel.associationRules.show()

if __name__=="__main__":
	timeoutpidsmap=[(10,[1,2,3]),(11,[2,3,4,5]),(12,[7,5,8,9]),(19,[2,3,4,5,6,7]),(20,[1,2,5,6,7])]
	SurvivalIndexTimeout(timeoutpidsmap)
	processes_set_partitions([1,2,3,4,5,6,7,8,9])

