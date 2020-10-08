# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 19:25:26 2020

@author: marti
"""
from classes import *
from functions import play

dim = 3
size = 20
max_steps = 100
angle_between_steps = 6
frames_by_step = 2
output_path = "pngs/step"

rules = wxyzRules(2,3,3,3) 
 
grid = Grid(dim,size)

###---CUSTOMISATION---###
grid.addCell((9,9,8))
grid.addCell((9,9,9))
grid.addCell((9,9,10))
grid.addCell((9,8,9))
grid.addCell((9,10,9))
###-------------------###

play(grid,rules,max_steps,True,output_path,angle_between_steps,frames_by_step)