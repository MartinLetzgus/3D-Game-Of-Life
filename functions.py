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

def play(grid,rules,max_steps=1000,save_pictures=True,output_path='',angle_between_steps=6,frames_by_step=2):
    alive = grid.count_cells_alive()
    print(alive)
    liste = [alive]
    i=0
    angle = 0
    while(alive>0 and i<(max_steps)):
        if(save_pictures and grid.dim==3):
            for ii in range (frames_by_step):
                output_name = output_path+str(i)+"_"+str(ii)+'.png'
                grid.save3D(colorz,output_name,angle)
                angle += angle_between_steps/frames_by_step
        elif(save_pictures and grid.dim==2):
            grid.save2D(['white', 'yellow', 'orange','darkorange','red'],output_path+str(i)+'.png')
        grid.nextStep(rules)
        alive = grid.count_cells_alive()
        liste.append(alive)
        i+=1
        print(alive)