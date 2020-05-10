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
from pyspark.mllib.feature import Word2Vec

#reference: https://spark.apache.org/docs/latest/ml-collaborative-filtering.html

if __name__=="__main__":
	spsess=SparkSession.builder.master("local").appName("Publications_Word2Vec").getOrCreate()
	#lines1 = spsess.read.text("Spark_Word2Vec_GoogleScholar.txt").rdd
	lines1 = spsess.read.text("Spark_Word2Vec_SemanticScholar.txt").rdd
	lines2 = spsess.read.text("Spark_Word2Vec_DBLP.txt").rdd
	words1 = lines1.map(lambda row: row.value.split(" "))
	words2 = lines2.map(lambda row: row.value.split(" "))
	print("words1:",words1.collect())
	print("words2:",words2.collect())
	word2vec = Word2Vec()
	word2vec.setVectorSize(10)
	word2vec.setSeed(100)
	model1 = word2vec.fit(words1)
	model2 = word2vec.fit(words2)
	vectors1 = model1.getVectors()
	vectors2 = model2.getVectors()
	print("vectors1:",vectors1)
	print("vectors2:",vectors2)
	synonyms1 = model1.findSynonyms("of",5)
	synonyms2 = model2.findSynonyms("=",5)
	for w,cosdist in synonyms1:
		print("synonym1:",w," - cosine distance:",cosdist) 
	for w,cosdist in synonyms2:
		print("synonym2:",w," - cosine distance:",cosdist) 

