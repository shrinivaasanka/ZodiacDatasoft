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
from pyspark.sql import DataFrameStatFunctions as dfsfunc
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.recommendation import ALS
from pyspark.sql import Row

#reference: https://spark.apache.org/docs/latest/ml-collaborative-filtering.html

if __name__=="__main__":
	spsess=SparkSession.builder.master("local").appName("RecommenderSystems").getOrCreate()

	lines = spsess.read.text("AdvertisementAnalytics_RecommenderSystemsCF.txt").rdd
	fields = lines.map(lambda row: row.value.split("-"))
	namedfields = fields.map(lambda p: Row(viewerId=int(p[0]), channelId=int(p[1]),
                                     rating=float(p[2]), timestamp=long(p[3])))
	ratings = spsess.createDataFrame(namedfields)
	(training, test) = ratings.randomSplit([0.8, 0.2])

	als = ALS(maxIter=5, regParam=0.01,userCol="viewerId",itemCol="channelId",ratingCol="rating",
          coldStartStrategy="drop")
	model = als.fit(training)
	predictions = model.transform(test)
	print "training:",training.collect()
	print "test:",test.collect()
	print "predictions:",predictions.collect()
	evaluator = RegressionEvaluator(metricName="rmse", labelCol="rating",
                                predictionCol="prediction")
	if predictions.collect() != []:
		rmse = evaluator.evaluate(predictions)
	userRecs = model.recommendForAllUsers(10)
	channelRecs = model.recommendForAllItems(10)
	print "userRecs:",userRecs.collect()
	print "channelRecs:",channelRecs.collect()
	
