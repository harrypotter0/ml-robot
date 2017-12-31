'''
Belief = Probability

measurement = Bayes Rule = Sense = Product followed by Normalization
motion = Total Probability= Move = Convolution ( Addition )

Normalization :: EP(Xi)=1
0<=P(X)<=1
P(X1)=0.2 , P(X2)=0.8

Bayes' Rule ::
X = grid cells Z= measurements
p(X|Z) = (p(Z/X)p(X))/p(Z)
'''
p=[0.2,0.2,0.2,0.2,0.2]
world=['green','red','red','green','green','green']
measurements = ['red','red']
motions = [1,1]
pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

def sense(p,Z):
    q=[]
    for i in range(len(p)):
        hit = (Z==world[i])
        q.append(p[i]*(hit*pHit+(1-hit)*pMiss))
    s = sum(q)
    for i in range(len(p)):
        q[i] = q[i]/s
    return q

def move(p,U):
    q=[]
    for i in range(len(p)):
        s = pExact * p[(i-U)%len(p)]
        s = s + pOvershoot * p[(i-U-1)%len(p)]
        s = s + pUndershoot * p[(i-U+1)%len(p)]
        q.append(s)
    return q

#for k in range(len(measurements)):
#    p = sense(p, measurements[k])

for k in range(len(measurements)):
    p = sense(p,measurements[k])
    p = move(p,motions[k])

print p
