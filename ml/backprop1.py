import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#iterations
epochs = 10000

#learn rate
alpha = 0.01

#weights
w1 = 1
w2 = 1
w3 = 1
w4 = 1
w5 = 1
w6 = 1
w7 = 1
w8 = 1
w9 = 1
w10= 1

#bias
b1 = 1
b2 = 1

#input
x1 = 1
x2 = 20
x3 = 50

#target
t1 = 0.1
t2 = 0.8


# Activation (sigmoid) function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

class Perceptron:
    def __init__(self,X,w,activation = None):
        self.X = X
        self.w = w
        self.activation = activation

    def out(self):
        self.zh()
        self.h = self.activation(self.net)
        return self.h

    def zh(self):
        self.net = np.dot(self.X, self.w)

def forwardProp(x1,x2,x3,w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,b1,b2):

    p1 = Perceptron([x1,x2,x3,1],[w1,w3,w5,b1],sigmoid)
    p2 = Perceptron([x1,x2,x3,1],[w2,w4,w6,b1],sigmoid)
    p3 = Perceptron([p1.out(),p2.out(),1],[w7,w9,b2],sigmoid)
    p4 = Perceptron([p1.out(),p2.out(),1],[w8,w10,b2],sigmoid)

    h1 = p1.out()
    h2 = p2.out()
    o1 = p3.out()
    o2 = p4.out()

    return h1, h2, o1, o2

def gradients(h1, h2, o1, o2):

    #gradients of weights
    dE_dw7  = (o1-t1)*o1*(1-o1)*h1
    dE_dw8  = (o2-t2)*o2*(1-o2)*h1
    dE_dw9  = (o1-t1)*o1*(1-o1)*h2
    dE_dw10 = (o2-t2)*o2*(1-o2)*h2

    dE_dw1 = (o1-t1)*o1*(1-o1)*w7 *h1*(1-h1)*x1 + \
             (o2-t2)*o2*(1-o2)*w8 *h1*(1-h1)*x1
    dE_dw2 = (o1-t1)*o1*(1-o1)*w9 *h2*(1-h2)*x1 + \
             (o2-t2)*o2*(1-o2)*w10*h2*(1-h2)*x1
    dE_dw3 = (o1-t1)*o1*(1-o1)*w7 *h1*(1-h1)*x2 + \
             (o2-t2)*o2*(1-o2)*w8 *h1*(1-h1)*x2
    dE_dw4 = (o1-t1)*o1*(1-o1)*w9 *h2*(1-h2)*x2 + \
             (o2-t2)*o2*(1-o2)*w10*h2*(1-h2)*x2
    dE_dw5 = (o1-t1)*o1*(1-o1)*w7 *h1*(1-h1)*x3 + \
             (o2-t2)*o2*(1-o2)*w8 *h1*(1-h1)*x3
    dE_dw6 = (o1-t1)*o1*(1-o1)*w9 *h2*(1-h2)*x3 + \
             (o2-t2)*o2*(1-o2)*w10*h2*(1-h2)*x3

    dE_db1 = (o1-t1)*o1*( w7*h1*(1-h1) +  w9*h2*(1-h2) ) + \
             (o2-t2)*o2*( w8*h1*(1-h1) + w10*h2*(1-h2) )
    dE_db2 = (o1-t1)*o1*(1-o1) + (o2-t2)*o2*(1-o2)

    if(False):
        print("dE_dw1",dE_dw1)
        print("dE_dw2",dE_dw2)
        print("dE_dw3",dE_dw3)
        print("dE_dw4",dE_dw4)
        print("dE_dw5",dE_dw5)
        print("dE_dw6",dE_dw6)
        print("dE_dw7",dE_dw7)
        print("dE_dw8",dE_dw8)
        print("dE_dw9",dE_dw9)
        print("dE_dw10",dE_dw10)
        print("dE_db1",dE_db1)
        print("dE_db2",dE_db2)

    return dE_dw1, dE_dw2, dE_dw3, dE_dw4, dE_dw5, dE_dw6, dE_dw7, dE_dw8, dE_dw9, dE_dw10, dE_db1, dE_db2 


def error(oList, tList):
        return 0.5 * (np.power(oList[0] - tList[0], 2) + np.power(oList[1] - tList[1], 2))


errList = []

for i in range(epochs):
    h1, h2, o1, o2 = forwardProp(x1,x2,x3,w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,b1,b2)
    dE_dw1, dE_dw2, dE_dw3, dE_dw4, dE_dw5, dE_dw6, dE_dw7, dE_dw8, dE_dw9, dE_dw10, dE_db1, dE_db2 = gradients(h1, h2, o1, o2)

    #compute error
    sse = error([o1, o2], [t1, t2])
    errList.append(sse)

    #update weights
    w1  = w1  - alpha * dE_dw1
    w2  = w2  - alpha * dE_dw2
    w3  = w3  - alpha * dE_dw3
    w4  = w4  - alpha * dE_dw4
    w5  = w5  - alpha * dE_dw5
    w6  = w6  - alpha * dE_dw6
    w7  = w7  - alpha * dE_dw7
    w8  = w8  - alpha * dE_dw8
    w9  = w9  - alpha * dE_dw9
    w10 = w10 - alpha * dE_dw10
    b1  = b1  - alpha * dE_db1
    b2  = b2  - alpha * dE_db2

print("Final result:")
print("Targets:",t1,t2)
print("Outputs:",o1,o2)
print("Final weights:",w1,w2,w3,w4,w5,w6,w7,w8,w9,w10)

pd.DataFrame(errList, columns=['SSE']).plot()
plt.savefig("sse.png")
plt.show()
