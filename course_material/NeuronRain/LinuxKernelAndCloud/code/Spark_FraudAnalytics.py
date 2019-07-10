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

if __name__=="__main__":
    spsess=SparkSession.builder.master("local").appName("Fraud Analytics").getOrCreate()
    df=spsess.read.format("csv").option("header","true").load("creditcard.csv")
    identity=sorted(df.groupBy(["V1","V2","V3","V4","V5","V6","V7","V8","V9"]).agg({'Amount':'avg'}).collect())
    print "Average amount withdrawn per cardholder:",identity 
    dffreq=dfsfunc(df).freqItems(["V1","V2","V3","V4","V5","V6","V7","V8","V9","Amount"]).collect()
    print "Frequent Items :",dffreq
    dfstat=df.describe(["V1","V2","V3","V4","V5","V6","V7","V8","V9","Amount"]).show()

