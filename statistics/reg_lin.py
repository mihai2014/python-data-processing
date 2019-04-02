import numpy as np

class reg_lin:
    def __init__(self,data):
        self.data = data
        self.line2()

    def line1(self):
        #transpose data
        x, y = self.data.T

        #population
        DDOF = 0

        #mean
        x_m = np.mean(x)
        y_m = np.mean(y)

        #std. dev. 
        s_x = np.std(x,ddof=DDOF)
        s_y = np.std(y,ddof=DDOF)

        #corelation coef
        r = np.corrcoef(x,y)[0,1]

        #slope of regression line
        m = r * s_y/s_x

        #y intercept
        n = y_m - m*x_m
        #print("y = % sx + %s" % (m,n))

        self.m = m
        self.n = n

        return(m,n)

    def line2(self):
        #transpose data
        x, y = self.data.T

        xy = np.multiply(x,y)
        xx = np.multiply(x,x)

        x_m = np.mean(x)
        y_m = np.mean(y)
        xy_m = np.mean(xy)
        xx_m = np.mean(xx)

        m = (xy_m - x_m * y_m )/(xx_m - x_m * x_m)
        n = y_m - m * x_m

        self.m = m
        self.n = n

        return(m,n) 





