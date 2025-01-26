import numpy as np
import cv2
import random
import matplotlib.pyplot as plt


class jar:
    def __init__(self, width, breadth, height):
        self.width = width
        self.breadth = breadth
        self.height = height

        self.numGrains = self.width*self.breadth * self.height

        self.jar = np.zeros((self.width, self.breadth, self.height))

    def innoculate(self, number):
        for i in range(number):
            x, y, z = random.randint(0, self.width-1), random.randint(0, self.breadth-1), random.randint(0, self.height-1)
            if self.jar[x,y,z] == 1:
                i -= 1
            else:
                self.jar[x,y,z] = 1

    def grow(self):
        newJar = np.zeros((self.width+2, self.breadth+2, self.height+2))
        
        for x in range(self.width):
            for y in range(self.breadth):
                for z in range(self.height):
                    if self.jar[x,y,z] == 1:
                        newJar[x+1,y+1,z+1] = 1
                        
                        newJar[x+2,y+1,z+1] = 1
                        newJar[x,y+1,z+1] = 1
                        newJar[x+1,y+2,z+1] = 1
                        newJar[x+1,y,z+1] = 1
                        newJar[x+1,y+1,z+2] = 1
                        newJar[x+1,y+1,z] = 1

        newJar = newJar[1:self.width+1, 1:self.breadth+1, 1:self.height+1]
        return newJar
    
    def clear(self):
        self.jar = np.zeros((self.width, self.breadth, self.height))

w, b, h = 5,5,10
percentThrough = 1
maxInnoc = int((w*b*h)*percentThrough)
xs = list(range(0, maxInnoc)) # # of innoculation points
ys = [0]*maxInnoc# # of days to collonize
numTrials = 100

for trial in range(numTrials):
    for x in range(1, maxInnoc):

        myJar = jar(w,b,h)
        myJar.innoculate(1)

        time = 0
        while ( myJar.jar.sum() < x):
            myJar.jar = myJar.grow()
            time += 1

        myJar.clear()
        myJar.innoculate(x)

        while (myJar.jar.sum() != myJar.jar.size):
            myJar.jar = myJar.grow()
            time+=1

        

        ys[x] += time/numTrials


     
    

plt.plot(np.linspace(0,percentThrough,maxInnoc), ys)
plt.show()