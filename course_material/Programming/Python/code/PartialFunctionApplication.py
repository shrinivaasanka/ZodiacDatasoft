##############################################################################################################################################
#<a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/">Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a>.
###############################################################################################################################################
#Course Authored By:
#-----------------------------------------------------------------------------------------------------------
#Srinivasan Kannan
#(also known as: Shrinivaasan Kannan, Shrinivas Kannan)
#Ph: 9791499106, 9003082186
#Krishna iResearch Open Source Products Profiles:
#http://sourceforge.net/users/ka_shrinivaasan,
#https://github.com/shrinivaasanka,
#https://www.openhub.net/accounts/ka_shrinivaasan
#Personal website(research): https://sites.google.com/site/kuja27/
#emails: ka.shrinivaasan@gmail.com, shrinivas.kannan@gmail.com,
#kashrinivaasan@live.com
#-----------------------------------------------------------------------------------------------------------
##############################################################################################################################################

from functools import partial

def function1(a,b,c,d,e,f):
	print a,b,c,d,e,f

if __name__=="__main__":
	partialfunction1=partial(function1,1)
	partialfunction2=partial(partialfunction1,2)
	partialfunction2=partial(partialfunction1,2)
	partialfunction3=partial(partialfunction2,3)
	partialfunction4=partial(partialfunction3,4)
	partialfunction5=partial(partialfunction4,5)
	partialfunction6=partial(partialfunction5,6)

	print "========================================="
	print "Equivalent Partially applied functions"
	print "========================================="
	partialfunction1(2,3,4,5,6)
	partialfunction2(3,4,5,6)
	partialfunction3(4,5,6)
	partialfunction4(5,6)
	partialfunction5(6)
	partialfunction6()
