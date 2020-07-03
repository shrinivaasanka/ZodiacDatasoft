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

def population_count(byte):
    intbyte=byte
    print("intbyte:",intbyte)
    sumbyte = 0
    for n in xrange(len(byte)):
        bit = int(intbyte[n])
        #print("bit:",bit)
        sumbyte = (sumbyte + bit)
    print("sumbyte:",sumbyte)
    return sumbyte

def mapbitstream(byte):
    sumbyte=population_count(byte)
    return sumbyte 

def reducebitstream(sumbyte1,sumbyte2):
    return sumbyte1 + sumbyte2 

if __name__=="__main__":
    spsess=SparkSession.builder.master("local[4]").appName("Population Count").getOrCreate()
    df=spsess.read.format("csv").load("Spark_PopulationCount.csv")
    bitstream=df.collect()
    print(bitstream[0]["_c0"])
    bs=bitstream[0]["_c0"]
    start=0
    end=32
    bsarray=[]
    while start <= len(bs) and end <= len(bs):
        bsarray.append(bs[start:end])
        start+=32
        if start >= len(bs):
            break
        end+=32
        if end >= len(bs):
            end = len(bs)
    print("bsarray:",bsarray)
    sum=spsess.sparkContext.parallelize(bsarray).map(mapbitstream).reduce(reducebitstream)
    print("Population count(number of 1s) in bit stream:",sum)
