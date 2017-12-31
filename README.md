# ml-robotics

1.  Localization
2.  Kalman Filters
3.  Particle Filters
4.  Search
5.  PID Control
6.  SLAM

* Project: Runaway Robot


## Key Points in Robotics ::
* The less the value of the cv , more is the certainity of teh localization
* 1--> prior 2--> measurement Probability
* new mean(mu2) lies b/w the prior and the next mean
* m' = (1/(cv1+cv2)*[cv1*mean2+cv2*mean1])

* new co-variance(sigma2) is more certain than the previous two co-variances
* cv' = 1/(1/(cv1)+1/(cv2))

* Belief = Probability

* measurement = Bayes Rule = Sense = Product followed by Normalization
* motion = Total Probability= Move = Convolution ( Addition )

* Normalization :: EP(Xi)=1
* 0<=P(X)<=1
* P(X1)=0.2 , P(X2)=0.8

## Bayes' Rule ::
* X = grid cells Z= measurements
* p(X|Z) = (p(Z/X)p(X))/p(Z)
