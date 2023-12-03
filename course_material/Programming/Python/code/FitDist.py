##############################################################################################################################################
# <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/">Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a>.
###############################################################################################################################################
# Course Authored By:
# -----------------------------------------------------------------------------------------------------------
##############################################################################################################################################
# K.Srinivasan
# NeuronRain Documentation and Licensing: http://neuronrain-documentation.readthedocs.io/en/latest/
# Personal website(research): https://acadpdrafts.readthedocs.io
##############################################################################################################################################

import scipy
import matplotlib.pyplot as plt
from scipy.stats import rv_discrete,rv_continuous
import inspect

def fit_distribution(data):
    distributions=inspect.getmembers(scipy.stats)
    print(distributions)
    bounds=[(0,100),(0,100)]
    for d in distributions:
        if isinstance(d[1],scipy.stats.rv_continuous) or isinstance(d[1],scipy.stats.rv_discrete): 
            try:
                print(type(d[1]))
                dist=d[1]
                dist=scipy.stats.fit(dist,data,bounds)
                print("dist.params:",dist.params)
                dist.plot()
                plt.show()
            except Exception as ex:
                print(ex)

if __name__=="__main__":
    fit_distribution([1,2,3,4,4,55,4,22,23,78,1,2,4,1,2,3,2,13,34,23,12,3,23,20,21,25,24,23,6,3,2])
