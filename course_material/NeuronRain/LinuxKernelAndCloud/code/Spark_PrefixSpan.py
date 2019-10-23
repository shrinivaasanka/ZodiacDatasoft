##############################################################################################################################################
#<a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/">Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a>.
##############################################################################################################################################
#Course Authored By:
#-----------------------------------------------------------------------------------------------------------
#K.Srinivasan
#NeuronRain Documentation and Licensing: http://neuronrain-documentation.readthedocs.io/en/latest/
#Personal website(research): https://sites.google.com/site/kuja27/
#-----------------------------------------------------------------------------------------------------------

from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.sql import DataFrame as df
from pyspark.ml.fpm import PrefixSpan

#reference: https://spark.apache.org/docs/latest/ml-frequent-pattern-mining.html

if __name__=="__main__":
	spsess=SparkSession.builder.master("local").appName("PrefixSpan").getOrCreate()
	lines = spsess.read.text("/media/Krishna_iResearch_/Krishna_iResearch_OpenSource/GitHub/asfer-github-code/python-src/asfer.enchoros.seqmining").rdd
	sequences = lines.map(lambda row: row.value.split("#"))
	rows=[]
	for seq in sequences.collect():
		seqarray=[]
		for s in seq:
			seqarray.append(list(s))
		rows.append(Row(sequence=seqarray))
	df=spsess.sparkContext.parallelize(rows).toDF()
	print df.collect()
	prefixSpan = PrefixSpan(minSupport=0.2, maxPatternLength=3,
                        maxLocalProjDBSize=32000000)
	# Find frequent sequential patterns.
	print "Frequent Patterns in Astronomical Dataset (encoded degree range positions of celestial bodies - planets spread across 12 houses of 30 degrees each) by PrefixSpan:"
	freqpatterns=prefixSpan.findFrequentSequentialPatterns(df).show()

	
