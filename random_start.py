# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 01:45:22 2020

@author: martin
"""
from classes import *
from functions import play

dim = 3
size = 20
random_start = 0.1
max_steps = 100
angle_between_steps = 6
frames_by_step = 2
output_path = "pngs/radom_start"

rules = wxyzRules(2,3,3,3) 
 
grid = Grid(dim,size)
grid.fillRandom(random_start)

play(grid,rules,max_steps,True,output_path,angle_between_steps,frames_by_step)
