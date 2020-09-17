from classes import *
from mpl_toolkits import mplot3d
import numpy as np
from itertools import product, combinations
import matplotlib.pyplot as plt

def colorz(x):
    if x==1:
        return('yellow')
    elif x==2:
        return('orange')
    elif x==3:
        return('darkorange')
    else:
        return('red')

def play(grid,rules,save_pictures=True,angle_between_steps=6,frames_by_step=2):
    alive = grid.count_cells_alive()
    liste = [alive]
    i=0
    angle = 0
    while(alive>0 and i<(max_steps)):
        grid.nextStep(rules)
        alive = grid.count_cells_alive()
        liste.append(alive)
        i+=1
        if(save_pictures):
            fig = plt.figure()
            ax = plt.axes(projection='3d')    
            ax.set_xlim(0,size+1)
            ax.set_ylim(0,size+1)
            ax.set_zlim(0,size+1)
            ax.set_axis_off()
            for x in range (size):
                for y in range(size):
                    for z in range (size):
                        if grid.array[x,y,z]!=0: 
                            color = colorz(grid.array[x,y,z])
                            r = [-0.5,0.5]
                            X, Y = np.meshgrid(r, r)
                            ax.plot_surface(X+x+0.5,Y+y+0.5,np.atleast_2d(0.5)+z+0.5, alpha=0.5, color=color)
                            ax.plot_surface(X+x+0.5,Y+y+0.5,np.atleast_2d(-0.5)+z+0.5, alpha=0.5, color=color)
                            ax.plot_surface(X+x+0.5,np.atleast_2d(-0.5)+y+0.5,Y+z+0.5, alpha=0.5, color=color)
                            ax.plot_surface(X+x+0.5,np.atleast_2d(0.5)+y+0.5,Y+z+0.5, alpha=0.5, color=color)
                            ax.plot_surface(np.atleast_2d(0.5)+x+0.5,X+y+0.5,Y+z+0.5, alpha=0.5, color=color)
                            ax.plot_surface(np.atleast_2d(-0.5)+x+0.5,X+y+0.5,Y+z+0.5, alpha=0.5, color=color)
            for ii in range (frames_by_step):
                ax.view_init(elev=10., azim=angle)
                plt.savefig("pngs/step_"+str(i)+"_"+str(ii)+".png")
                angle += angle_between_steps/frames_by_step
            plt.clf()
        
dim = 3
size = 25
random_start = 0.1
max_steps = 200
angle_between_steps = 6
frames_by_step = 2

rules = wxyzRules(2,3,3,3) 

 
grid = BasicGrid(dim,size)
grid.fillRandom(random_start)
play(grid,rules,angle_between_steps,frames_by_step)