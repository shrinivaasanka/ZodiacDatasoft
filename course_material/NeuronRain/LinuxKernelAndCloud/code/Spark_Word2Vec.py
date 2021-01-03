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
from Transformers import Transformers

# reference: https://spark.apache.org/docs/latest/api/python/pyspark.ml.html?highlight=word2vec


def tokenize(row):
    words = row.value.split(" ")
    words = [[w] for w in words if w != '']
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
    word2vec.setVectorSize(3)
    word2vec.setSeed(42)
    words1rdd = spsess.sparkContext.parallelize(words1)
    print(("words1rdd:", words1rdd.collect()))
    words1df = spsess.createDataFrame(words1rdd, StringType())
    words1df.show()
    words1df.printSchema()
    model1 = word2vec.fit(words1rdd)
    vectors1 = model1.getVectors()
    print("=================")
    print(("Concept Cloud:"))
    print("=================")
    print("vectors1:",vectors1)
    word2vecembeddings_vec=[]
    for concept,vector in vectors1.items():
        print("concept [",concept,"] is embedded at ",vector)
        word2vecembeddings_vec.append(vector)
    try:
        synonyms1 = model1.findSynonyms(pattern, 5)
        for w, cosdist in synonyms1:
            print(("synonym1:", w, " - cosine distance:", cosdist))
    except:
        print(("pattern [", pattern, "] not in word2vec vocabulary"))
    return word2vecembeddings_vec

if __name__ == "__main__":
    word2vecembeddings=bibliometric_word2vec("Spark_Word2Vec_SemanticScholar.txt","merit")
    if len(word2vecembeddings) >= 3:
        print("word2vecembeddings:",word2vecembeddings[:3])
        tf=Transformers(word2vecembeddings[:3],[[0.41,0.42,0.43],[0.41,0.3,0.45],[0.43,0.4,0.5]],[[0.4,0.55,0.76],[0.1,0.83,0.5],[0.3,0.4,0.25]],[[0.7,0.8,0.9],[0.1,0.8,0.5],[0.3,0.2,0.9]],[0.1,0.3,0.5],3)
        tf.transformers_attention_sequence_model(0.1,0.8)
    word2vecembeddings=bibliometric_word2vec("Spark_Word2Vec_GoogleScholar.txt","merit")
    if len(word2vecembeddings) >= 3:
        print("word2vecembeddings:",word2vecembeddings[:3])
        tf=Transformers(word2vecembeddings[:3],[[0.41,0.42,0.43],[0.41,0.3,0.45],[0.43,0.4,0.5]],[[0.4,0.55,0.76],[0.1,0.83,0.5],[0.3,0.4,0.25]],[[0.7,0.8,0.9],[0.1,0.8,0.5],[0.3,0.2,0.9]],[0.1,0.3,0.5],3)
        tf.transformers_attention_sequence_model(0.1,0.8)
    word2vecembeddings=bibliometric_word2vec("Spark_Word2Vec_DBLP.txt","merit")
    if len(word2vecembeddings) >= 3:
        print("word2vecembeddings:",word2vecembeddings[:3])
        tf=Transformers(word2vecembeddings[:3],[[0.41,0.42,0.43],[0.41,0.3,0.45],[0.43,0.4,0.5]],[[0.4,0.55,0.76],[0.1,0.83,0.5],[0.3,0.4,0.25]],[[0.7,0.8,0.9],[0.1,0.8,0.5],[0.3,0.2,0.9]],[0.1,0.3,0.5],3)
        tf.transformers_attention_sequence_model(0.1,0.8)
    word2vecembeddings=bibliometric_word2vec("Spark_Word2Vec_MicrosoftAcademic.txt","merit")
    if len(word2vecembeddings) >= 3:
        print("word2vecembeddings:",word2vecembeddings[:3])
        tf=Transformers(word2vecembeddings[:3],[[0.41,0.42,0.43],[0.41,0.3,0.45],[0.43,0.4,0.5]],[[0.4,0.55,0.76],[0.1,0.83,0.5],[0.3,0.4,0.25]],[[0.7,0.8,0.9],[0.1,0.8,0.5],[0.3,0.2,0.9]],[0.1,0.3,0.5],3)
        tf.transformers_attention_sequence_model(0.1,0.8)
    word2vecembeddings=bibliometric_word2vec("Spark_Word2Vec_Bibliography.txt","merit")
    if len(word2vecembeddings) >= 3:
        print("word2vecembeddings:",word2vecembeddings[:3])
        tf=Transformers(word2vecembeddings[:3],[[0.41,0.42,0.43],[0.41,0.3,0.45],[0.43,0.4,0.5]],[[0.4,0.55,0.76],[0.1,0.83,0.5],[0.3,0.4,0.25]],[[0.7,0.8,0.9],[0.1,0.8,0.5],[0.3,0.2,0.9]],[0.1,0.3,0.5],3)
        tf.transformers_attention_sequence_model(0.1,0.8)
    word2vecembeddings=bibliometric_word2vec("Spark_Word2Vec_PublicationFullText.txt", "majority")
    if len(word2vecembeddings) >= 3:
        print("word2vecembeddings:",word2vecembeddings[:3])
        tf=Transformers(word2vecembeddings[:3],[[0.41,0.42,0.43],[0.41,0.3,0.45],[0.43,0.4,0.5]],[[0.4,0.55,0.76],[0.1,0.83,0.5],[0.3,0.4,0.25]],[[0.7,0.8,0.9],[0.1,0.8,0.5],[0.3,0.2,0.9]],[0.1,0.3,0.5],3)
        tf.transformers_attention_sequence_model(0.1,0.8)
    word2vecembeddings=bibliometric_word2vec("Spark_Word2Vec_PatentExample1.txt", "transaction")
    if len(word2vecembeddings) >= 3:
        print("word2vecembeddings:",word2vecembeddings[:3])
        tf=Transformers(word2vecembeddings[:3],[[0.41,0.42,0.43],[0.41,0.3,0.45],[0.43,0.4,0.5]],[[0.4,0.55,0.76],[0.1,0.83,0.5],[0.3,0.4,0.25]],[[0.7,0.8,0.9],[0.1,0.8,0.5],[0.3,0.2,0.9]],[0.1,0.3,0.5],3)
        tf.transformers_attention_sequence_model(0.1,0.8)
    word2vecembeddings=bibliometric_word2vec("Spark_Word2Vec_PatentExample2.txt", "transaction")
    if len(word2vecembeddings) >= 3:
        print("word2vecembeddings:",word2vecembeddings[:3])
        tf=Transformers(word2vecembeddings[:3],[[0.41,0.42,0.43],[0.41,0.3,0.45],[0.43,0.4,0.5]],[[0.4,0.55,0.76],[0.1,0.83,0.5],[0.3,0.4,0.25]],[[0.7,0.8,0.9],[0.1,0.8,0.5],[0.3,0.2,0.9]],[0.1,0.3,0.5],3)
        tf.transformers_attention_sequence_model(0.1,0.8)
    word2vecembeddings=bibliometric_word2vec("Spark_Word2Vec_NASAADSHarvard.txt", "transaction")
    if len(word2vecembeddings) >= 3:
        print("word2vecembeddings:",word2vecembeddings[:3])
        tf=Transformers(word2vecembeddings[:3],[[0.41,0.42,0.43],[0.41,0.3,0.45],[0.43,0.4,0.5]],[[0.4,0.55,0.76],[0.1,0.83,0.5],[0.3,0.4,0.25]],[[0.7,0.8,0.9],[0.1,0.8,0.5],[0.3,0.2,0.9]],[0.1,0.3,0.5],3)
        tf.transformers_attention_sequence_model(0.1,0.8)
