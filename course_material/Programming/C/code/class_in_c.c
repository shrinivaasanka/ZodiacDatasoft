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
*/

#include <stdio.h>

struct variable
{
	int private;
	union
	{
		int x1;
		float x2;
	};
};

struct classinc
{
	struct variable pub_variable;
	struct variable priv_variable;
	void (*setint)(struct variable* var,int value);
	void (*setfloat)(struct variable* var,float value);
	int (*function1)(struct classinc* cinc, float arg1, double arg2);
};

void setint(struct variable* var,int value)
{
	if(var->private==0)
	{
		printf("setint(): variable access \n");
		var->x1=value;
	}
	else
	{
		printf("setint(): private variable access denied \n");
	}
}

void setfloat(struct variable* var,float value)
{
	if(var->private==0)
	{
		printf("setfloat(): variable access \n");
		var->x2=value;
	}
	else
	{
		printf("setfloat(): private variable access denied \n");
	}
}

int f1(struct classinc* cinc,float arg1, double arg2)
{
	if(cinc->priv_variable.private==1)
		cinc->priv_variable.private=0;
	printf("classinc::f1(): Setting private variable priv_variable from function classinc::f1() \n");
	setfloat(&cinc->priv_variable, arg2);
	printf("classinc::f1(): arg1=%f, arg2=%f \n",arg1,arg2);
	cinc->priv_variable.private=1;
}

int main()
{
	struct classinc cinc;
	cinc.function1=f1;
	cinc.setint=setint;
	cinc.setfloat=setfloat;
	cinc.pub_variable.private=0;
	cinc.priv_variable.private=1;
	cinc.setint(&cinc.pub_variable,9128);
	cinc.setfloat(&cinc.priv_variable,8382.7);
	cinc.function1(&cinc,20121920.5,198289819289812.32);
	printf("cinc.pub_variable = %d, cinc.priv_variable.x2=%f \n",cinc.pub_variable.x1, cinc.priv_variable.x2);
}
