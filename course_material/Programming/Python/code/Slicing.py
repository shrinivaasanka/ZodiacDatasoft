##############################################################################################################################################
#<a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/">Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a>.
###############################################################################################################################################
#Course Authored By:
#-----------------------------------------------------------------------------------------------------------
#K.Srinivasan
#NeuronRain Documentation and Licensing: http://neuronrain-documentation.readthedocs.io/en/latest/
#Personal website(research): https://sites.google.com/site/kuja27/
#-----------------------------------------------------------------------------------------------------------
##############################################################################################################################################

from io import StringIO

if __name__=="__main__":
	text=u"1,2,3,4,5,6,7,8\n9,10,11,12,13,14,15,16\n"
	flag="ListComp"
	if flag == "Slicing":
		import numpy as np
		parsedarray=np.genfromtxt(StringIO(text),delimiter=",")
		slicedarray1=parsedarray[slice(0,3),slice(0,3)]
		print("slicedarray1 - slice() of equal slices:")
		print(slicedarray1)
		slicedarray2=parsedarray[slice(0,2),slice(0,3)]
		print("slicedarray2 - slice() of unequal slices:")
		print(slicedarray2)
		slicedarray3=parsedarray[slice(0,3),(0,3)]
		print("slicedarray3 - slice() and tuple:")
		print(slicedarray3)
		slicedarray4=parsedarray[slice(0,7,2),slice(0,7,2)]
		print("slicedarray4 - step slice() :")
		print(slicedarray4)
	else:
		parsedarray=text.split("\n")
		parsedarray=[row.split(",") for row in parsedarray if len(row) > 0]
		print(parsedarray)
		slicedarray5=[row[2:5] for row in parsedarray]
		print("slicedarray5 - list comprehension:")
		print(slicedarray5)
