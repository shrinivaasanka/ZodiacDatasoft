##############################################################################################################################################
# <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/">Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a>.
##############################################################################################################################################
# Course Authored By:
# -----------------------------------------------------------------------------------------------------------
# K.Srinivasan
# NeuronRain Documentation and Licensing: http://neuronrain-documentation.readthedocs.io/en/latest/
# Personal website(research): https://sites.google.com/site/kuja27/
# -----------------------------------------------------------------------------------------------------------

from pyspark.sql import SparkSession
from pyspark.mllib.feature import Word2Vec
from pyspark.sql.types import StringType
import pprint

# reference: https://spark.apache.org/docs/latest/api/python/pyspark.ml.html?highlight=word2vec


def tokenize(row):
    words = row.value.split(" ")
    words = [[w.encode("utf-8")] for w in words if w != '']
    print(("tokenize() - words:", words))
    return words


def concat(str1, str2):
    if str1 is not None and str2 is not None:
        return str1 + str2


def bibliometric_word2vec(bibliography, pattern):
    spsess = SparkSession.builder.master("local[4]").appName(
        "Publications_Word2Vec").getOrCreate()
    lines1 = spsess.read.text(bibliography).rdd
    words1 = lines1.map(tokenize).reduce(concat)
    print(("words1:", words1))
    word2vec = Word2Vec()
    word2vec.setVectorSize(5)
    word2vec.setSeed(42)
    words1rdd = spsess.sparkContext.parallelize(words1)
    print(("words1rdd:", words1rdd.collect()))
    words1df = spsess.createDataFrame(words1rdd, StringType())
    # words1df.show()
    words1df.printSchema()
    model1 = word2vec.fit(words1rdd)
    vectors1 = model1.getVectors()
    print("=================")
    print(("Concept Cloud:"))
    print("=================")
    for concept,vector in vectors1.iteritems():
        print("concept [",concept,"] is embedded at ",vector)
    try:
        synonyms1 = model1.findSynonyms(pattern, 5)
        for w, cosdist in synonyms1:
            print(("synonym1:", w, " - cosine distance:", cosdist))
    except:
        print(("pattern [", pattern, "] not in word2vec vocabulary"))


if __name__ == "__main__":
    bibliometric_word2vec("Spark_Word2Vec_SemanticScholar.txt","merit")
    bibliometric_word2vec("Spark_Word2Vec_GoogleScholar.txt","merit")
    bibliometric_word2vec("Spark_Word2Vec_DBLP.txt","merit")
    bibliometric_word2vec("Spark_Word2Vec_MicrosoftAcademic.txt","merit")
    bibliometric_word2vec("Spark_Word2Vec_Bibliography.txt","merit")
    bibliometric_word2vec("Spark_Word2Vec_PublicationFullText.txt", "majority")
    bibliometric_word2vec("Spark_Word2Vec_PatentExample1.txt", "transaction")
    bibliometric_word2vec("Spark_Word2Vec_PatentExample2.txt", "transaction")
