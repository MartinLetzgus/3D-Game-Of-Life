#ONLY WORK WITH DIM=3 (for the moment)

import numpy as np
from numpy import random
                    
class BasicGrid():
    def __init__(self,dim,size,array=0):
        self.dim = dim
        self.size = size
        self.array = np.zeros([size]*dim)
        
    def addCell(self,tuple_coord):
        assert self.dim == len(tuple_coord)
        self.array[tuple_coord] = 1
        
    def fillRandom(self,proba=0.5):
        new_array = np.zeros([self.size]*self.dim)
        for x in range (self.size):
            for y in range (self.size):
                for z in range (self.size):
                    if random.random()<proba:
                        self.addCell((x,y,z))
        
    def count_cells_alive(self):
        total = 0
        for x in range (self.size):
            for y in range (self.size):
                for z in range (self.size):
                    if(self.array[x,y,z] != 0):
                        total += 1
        return(total)        
        
    def nextStep(self,rules):
        new_array = np.copy(self.array)
        #for each cell of the array
        for x in range (self.size):
            for y in range (self.size):
                for z in range (self.size):
                    total_neighbours = 0
                    #for each neighbour of the cell
                    for x2 in range (-1,1):
                        for y2 in range (-1,1):
                            for z2 in range (-1,1):
                                if ((x-x2>=0)and(y-y2>=0)and(z-z2>=0)and(x-x2<self.size)and(y-y2<self.size)and(z-z2<self.size)and(self.array[x-x2,y-y2,z-z2]!=0)):
                                    total_neighbours += 1
                    if rules.applyRules(self.array[x,y,z],total_neighbours):
                        new_array[x,y,z] += 1
                    else:
                        new_array[x,y,z] = 0
        self.array = new_array

        
                        
                                
        

class Rules():
    def __init__(self,function):
        self.function = function
        
    def applyRules(self,t0,x):
        return(self.function(t0,x))
            
class wxyzRules(Rules):
    def __init__(self,w,x,y,z):
        self.w = w
        self.x = x
        self.y = y
        self.z = z
        
        def function(t0,n):
            return(((t0==0)and(y<=n)and(n<=z))or((t0!=0)and(w<=n)and(n<=x)))
        
        self.function = function
        




