import vector
import math
class triangle:
    def __init__(self, l1,l2):
        self.l1=l1
        self.l2=l2
        self.x_p=math.sqrt(pow(l1.x1-l2.x1,2)+pow(l1.y1-l2.y1,2))


    #return the ratio in which l1, l2 should be shortened by (using TALAS )
    # like that [move l1,move l2 ] list, those parameters will be used in moveLile function later.
    # x is the expected dist (between l1 and l2 edges)
    def talas(self, x ):
        tmp1=(self.l1.length*x)/self.x_p
        d1= self.l1.length-tmp1
        tmp2 = (self.l2.length * x) / self.x_p
        d2 = self.l2.length - tmp2
        return [d1,d2]