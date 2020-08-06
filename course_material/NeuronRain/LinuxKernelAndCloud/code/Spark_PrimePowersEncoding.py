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
import sys
import math
import subprocess
from complement import toint
import json

if __name__=="__main__":
    subprocess.call(["/home/ksrinivasan/spark-2.4.3-bin-hadoop2.7/bin/spark-submit",
                     "DiscreteHyperbolicFactorizationUpperbound_TileSearch_Optimized.py", sys.argv[1], sys.argv[2], "False"], shell=False)
    factorsfile = open(
        "testlogs/Spark_PrimePowersEncoding.factors")
    factors = json.load(factorsfile)
    print("Factors of 99333539509987274314748077777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777761444238267790503463029217 (2060 bits integer) are:",factors)


