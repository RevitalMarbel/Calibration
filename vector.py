import math
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import numpy as np
import triangle

class line:
    # x1=0
    # y1=0
    # x2=0
    # y2=0
    # angle=0
    # length=0
    def __init__(self,x1,y1,x2,y2):
        self.x1=x1
        self.x2=x2
        self.y1=y1
        self.y2=y2
        if(x2!=x1 ):
            self.angle=math.atan((y2-y1)/(x2-x1))
        else:
            self.angle=0
        self.length=math.sqrt(math.pow(x2-x1,2)+(math.pow(y2-y2,2)))
    #move x1 and y1 to new location, move along a line and maintain the angle
    def moveInLine(self , dist):
        self.x1=self.x1+ dist*math.cos(self.angle)
        self.y1=self.y1+ dist*math.sin(self.angle)
    def plotLine(self, ax,color):
        p1=[self.x1,self.x2]
        p2=[self.y1,self.y2]
        print (p1,p2)
        l = mlines.Line2D(p1,p2, color= color)
        ax.add_line(l)


#test:

cx=6
cy=8
ax = plt.gca()
l1=line(2,2,cx,cy)
l2=line(5,5,cx,cy)
trig=triangle(l1,l2)
trig.talas(0.7)
print (l1.x1, l1.angle ,l1.length)
l1.plotLine(ax, 'r')
l1.moveInLine(0.5)
print(l1.length)
#l3=line()
l2.plotLine(ax ,'b')
plt.plot()
plt.show()
