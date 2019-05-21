/*
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

This is a non-linearly organized, code puzzles oriented, continually updated set of course notes on Java language. This
complements NeuronRain course materials on Linux Kernel, Cloud, BigData Analytics and Machine Learning and covers
fundamentals of Java.
----------------------------------------------------------------------------------------------------------------------------
*/

import java.lang.Integer;

public final class LambdaExpressions
{
	interface FuncInterface
	{
		void print1toN(int N);
	}

	public void recursion(int x, FuncInterface fi)
	{
		fi.print1toN(x);
		if (x > 0)
		{
			recursion(x-1, fi);
		}
	}

	public static void main(String[] args)
	{
		int N = Integer.parseInt(args[0]);	
		LambdaExpressions le = new LambdaExpressions();
		FuncInterface fi = (x) -> { System.out.println(x);};
		le.recursion(N,fi);
	}
}

