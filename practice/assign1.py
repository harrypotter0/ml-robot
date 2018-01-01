'''

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
'''




colors = [['red', 'green' ,'green', 'red' ,'red'],
          ['red', 'red' ,'green', 'red' ,'red'],
          ['red', 'red' ,'green', 'green' ,'red'],
          ['red', 'red' ,'red', 'red' ,'red']
          ]

measurements = ['green', 'green' ,'green', 'green' ,'green']


motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]

sensor_right = 0.7
p_move = 0.8

sensor_wrong = 1.0 - sensor_right
p_stay = 1.0 - p_move

def sense(p,colors , measurement):
    aux = [[0.0 for row in range(len(p[0]))] for col in range(len(p))]
    s=0.0
    for i in range(len(p)):
        for j in range(len(p[i])):
            hit = (measurement == colors[i][j] )
            aux[i][j] = p[i][j] * (hit * sensor_right + (1-hit) * sensor_wrong)
            s += aux[i][j]
    for i in range(len(aux)):
        for j in range(len(p[i])):
            aux[i][j] /= s
    return aux

def move(p , motion):
    aux = [[0.0 for row in range(len(p[0]))]for col in range(len(p))]

    for i in range(len(p)):
        for j in range(len(p[i])):
            aux[i][j] = (p_move * p[(i-motion[0])%len(p)][(j-motion[1])%len(p[i])]) + (p_stay * p[i][j])
    return aux

def show(p):
    for i in range(len(p)):
        print p[i]

if len(measurements) != len(motions):
    raise ValueError, "error in size of measurement/motion vector "

pinit = 1.0 /float(len(colors))/float(len(colors[0]))
p = [[pinit for row in range(len(colors[0]))]for col in range(len(colors))]

for k in range(len(measurements)):
    p = move(p,motions[k])
    p = sense(p,colors,measurements[k])

show(p)
