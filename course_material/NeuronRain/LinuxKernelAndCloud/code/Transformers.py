##############################################################################################################################################
# <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/">Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a>.
##############################################################################################################################################
# Course Authored By:
# -----------------------------------------------------------------------------------------------------------
# K.Srinivasan
# NeuronRain Documentation and Licensing: http://neuronrain-documentation.readthedocs.io/en/latest/
# Personal website(research): https://sites.google.com/site/kuja27/
# -----------------------------------------------------------------------------------------------------------

import numpy as np
import math
from Transformers_PerceptronAndGradient import LinearPerceptronGradient

class Transformers(object):
    def __init__(self,wordembedding,queries,keys,values,expected,dimension):
        self.embedding = np.array(wordembedding)
        self.query_weights = np.array(queries)
        self.key_weights = np.array(keys)
        self.value_weights = np.array(values)
        self.keyvector_dim = dimension
        self.expected = np.array(expected)
        self.attention = []

    def softmax(self,weights):
        newweights=[]
        weightslist=weights.tolist()
        for r in weightslist:
            newrow=[]
            for c in r: 
                newrow.append(math.exp(c))
            newrow = np.array(newrow)/sum(newrow)
            newweights.append(newrow.tolist())
        print("softmax(): newweights = ",newweights)
        return np.array(newweights)

    def transformers_attention_sequence_model(self,rho,bias):
        self.attention = np.matmul(self.query_weights,self.key_weights.T)/np.sqrt(self.keyvector_dim)
        self.attention = self.softmax(self.attention)
        self.attention = np.matmul(self.attention,self.value_weights)
        print("transformers_attention_sequence_model() - attention:",self.attention)
        for row in range(self.query_weights.shape[1]):
            self.query_weights[row]=LinearPerceptronGradient(self.expected.tolist(),self.query_weights[row].tolist(),rho,bias,self.attention.tolist())
        print("Learnt Query Weights:",self.query_weights)
        for row in range(self.key_weights.shape[1]):
            self.key_weights[row]=LinearPerceptronGradient(self.expected.tolist(),self.key_weights[row].tolist(),rho,bias,self.attention.tolist())
        print("Learnt Key Weights:",self.key_weights)
        for row in range(self.value_weights.shape[1]):
            self.value_weights[row]=LinearPerceptronGradient(self.expected.tolist(),self.value_weights[row].tolist(),rho,bias,self.attention.tolist())
        print("Learnt Values Weights:",self.value_weights)

if __name__=="__main__":
    tf=Transformers([[1,2,3],[4,5,6],[6.1,9.2,10.3]],[[1,2,3],[0.1,0.3,0.5],[3,4,5]],[[4,5,6],[0.1,0.3,0.5],[3,4,5]],[[7,8,9],[0.1,0.3,0.5],[3,4,5]],[0.1,0.3,0.5],3)
    tf.transformers_attention_sequence_model(0.1,0.8)
