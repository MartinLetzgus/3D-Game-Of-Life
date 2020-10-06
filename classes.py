import numpy as np
from numpy import random
                    
class Grid():
    def __init__(self,dim,size,array=0):
        self.dim = dim
        self.size = size
        self.array = np.zeros([size]*dim)
        
    class iterCells():
        #This iterator allows us to look for each cell of the grid
        def __init__(self, dim, size, start=0):
            self.num = start
            self.dim = dim
            self.size = size
            coord = ()
            n = self.num
            for d in range (dim):
                coord = coord + (int(n%size),)
                n = n - n%size
                n = n/size
            self.coord = coord
    
        def __iter__(self):
            return self
    
        def __next__(self):
            if self.num<self.size**self.dim:
                c = self.coord
                self.num += 1
                coord = ()
                n = self.num
                for d in range (self.dim):
                    coord = coord + (int(n%self.size),)
                    n = n - n%self.size
                    n = n/self.size
                self.coord = coord
                return c
            else:
                raise StopIteration
                      
    class iterNeighbours():
    #This iterator allows us to look for each neighboor of a cell
        def __init__(self, dim, size, tuple_coord, start =0):
            self.center = tuple_coord
            self.dim = dim
            self.size = size
            self.num = start
            self.coord = tuple([i-1 if (i-1>=0) else i for i in tuple_coord])
    
        def __iter__(self):
            return self
    
        def __next__(self):
            if self.num<3**self.dim:
                coord = ()
                c = self.coord
                while(len(coord)!=len(self.coord)or(coord==self.center)):
                    self.num += 1
                    coord = ()
                    n = self.num
                    for d in range (self.dim):
                        if ((self.center[d] + (n%3)-1>=0) and (self.center[d] + (n%3)-1 < self.size)):
                            coord = coord + (int(self.center[d] + (n%3)-1),)
                        else:
                            break
                        n = n - n%3
                        n = n/3
                self.coord = coord
                return c
            else:
                raise StopIteration
        
    def addCell(self,tuple_coord):
        assert self.dim == len(tuple_coord)
        self.array[tuple_coord] = 1
        
    def fillRandom(self,proba=0.5):        
        for coord in iter(self.iterCells(self.dim,self.size)):
            if random.random()<proba:
                self.addCell(coord)
        
    def count_cells_alive(self):
        total = 0
        for coord in (self.iterCells(self.dim,self.size)):
            assert len(coord)==self.dim
            if(self.array[coord] != 0):
                total += 1
        return(total)        
        
    def nextStep(self,rules):
        new_array = np.copy(self.array)
        for coord in iter(self.iterCells(self.dim,self.size)):
            total_neighbours = 0
            #for each neighbour of the cell
            for coord_neigh in iter(self.iterNeighbours(self.dim,self.size,coord)):
                if(self.array[coord_neigh]!=0):
                    total_neighbours += 1
            if rules.applyRules(self.array[coord],total_neighbours):
                new_array[coord] += 1
            else:
                new_array[coord] = 0
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
        




