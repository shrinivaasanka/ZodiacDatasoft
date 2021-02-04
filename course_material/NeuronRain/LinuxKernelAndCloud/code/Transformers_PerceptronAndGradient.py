##############################################################################################################################################
# <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/">Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a>.
##############################################################################################################################################
# Course Authored By:
# -----------------------------------------------------------------------------------------------------------
# K.Srinivasan
# NeuronRain Documentation and Licensing: http://neuronrain-documentation.readthedocs.io/en/latest/
# Personal website(research): https://sites.google.com/site/kuja27/
# -----------------------------------------------------------------------------------------------------------

# Gradient Descent and Ascent for local minimum and maximum of a cost function
# -------------------------------
# Gradient iterative update rule:
# -------------------------------
# xnew = xold - rho*firstderivative for descent
# xnew = xold + rho*firstderivative for ascent

# Following is a generic approximation written for linear perceptrons of the form wx+b
# Above update rule is discretized as :
#wnew = wold - alpha*deltaw

import rpy2.robjects as robj

# For a linear non-sigmoid perceptron w1*x1+w2*x2+...+wn*xn+b  for which weights have to be updated by Gradient
# the L2 norm of the perceptron is differentiated wrt x1,x2,...,xn and deltaw is computed


def LinearPerceptronGradient(outputs, weights, rho, bias, variables):
    converged = False
    sum = 0.0
    iteration = 0
    while not converged and iteration < 1000:
        deltaw = []
        term = bias
        varnum = 0
        sum = 0.0
        # Example iteration for two variables:
        # -----------------------------------
        # for x1,x2,output in zip(x1s, x2s, outputs):
        #	term = bias + weights[0]*x1 + weights[1]*x2 - output
        #	term = term * x2
        #	sum = sum + term
        #deltaw2 = sum * 2
        # ------------------------------------------------------------------------------
        # Following iteration is generic for arbitrary number of variables
        # generalizing previous example for 2 variables
        # ------------------------------------------------------------------------------
        for cnt1 in range(len(variables[0])):
            for cnt2 in range(len(variables)-1):
                term += weights[cnt2]*variables[cnt2][cnt1]
            term = term - outputs[cnt1]
            term = term * variables[varnum][cnt1]
            sum = sum + term
            varnum += 1
            deltaw.append(sum * 2)
        for cnt in range(len(variables[0])):
            if compute_perceptron(weights, variables, outputs) == 1:
                print("LinearPerceptronGradient() weight update iteration: Descending")
                weights[cnt] = weights[cnt] - rho * deltaw[cnt]
            else:
                print("LinearPerceptronGradient() weight update iteration: Ascending")
                weights[cnt] = weights[cnt] + rho * deltaw[cnt]
            print("LinearPerceptronGradient() weight update iteration: weights[", cnt, "] = ", weights[cnt])
            print("LinearPerceptronGradient() weight update iteration: deltaw = ", deltaw)

        for cnt in range(len(weights)):
            if deltaw[cnt]*-1.0 < 0.0000001:
                converged = True
            else:
                converged = False
        print("weights updated after Gradient : ", weights)
        print("converged:",converged)
        iteration += 1
    return weights


def compute_perceptron(weights, variables, outputs):
    print("weights:",weights)
    print("variables:",variables)
    print("outputs:",outputs)
    for o in range(len(outputs)):
        sum = 0
        for w in range(len(weights)):
            sum = sum + weights[w]*variables[w][o]
        if (outputs[o] - sum) > 10:
            return 1
    return 0


if __name__ == "__main__":
    outputs = [10.0, 25.0, 30.0, 45.0, 275.0]
    weights = [1.0, 1.4, 2.5, 2.0, 5.0]
    rho = -0.8
    bias = 0.0
    variables = [[1.0, 2.0, 5.0, 6.0, 8.0], [1.0, 12.0, 5.0, 7.0, 18.0], [
        1.0, 22.0, 35.0, 7.0, 8.0], [1.0, 2.0, 5.0, 87.0, 88.0], [1.0, 12.0, 5.0, 7.0, 8.0]]
    LinearPerceptronGradient(outputs, weights, rho, bias, variables)
