'''
** The less the value of the cv , more is the certainity of teh localization**
1--> prior 2--> measurement Probability
new mean(mu2) lies b/w the prior and the next mean
m' = 1/(cv1+cv2)*[cv1*mean2+cv2*mean1]

new co-variance(sigma2) is more certain than the previous two co-variances
cv' = 1/(1/(cv1)+1/(cv2))

'''
from math import *
def f(mu, sigma2, x):
    return 1/sqrt(2.*pi*sigma2) * exp(-.5 * (x-mu)**2 /sigma2)

print f(10., 4. ,8.)
