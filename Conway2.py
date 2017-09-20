# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 16:55:15 2017

@author: mucs_b
"""

import numpy as np
import matplotlib.pyplot as plt
import copy

#space = np.random.randint(2, size=(100,100))

coordinates = [(int(round(x)),int(round(y))) for x,y in np.random.normal(10,5,(100,2))]

np.mean([i[0] for i in coordinates])
space = np.zeros(shape=(int(np.mean([i[1] for i in coordinates]))*2,int(np.mean([i[0] for i in coordinates]))*2))

for i in coordinates:
    try:
        space[i[0]][i[1]] = 1
    except IndexError:
        pass
        

#
#space[4][5] = 1
#space[3][4] = 1
#space[5][5] = 1
#space[5][4] = 1
#space[5][3] = 1

space_start = copy.deepcopy(space)


def fNeighcount(matrix,y,x,verbose = 0):
    neighboors = 0
    if verbose == 1:
        print('Alive: ' + str(matrix[y][x]))
    
    try:
        if verbose == 1:
            print(([y,x+1],matrix[y][x+1]))
        neighboors += matrix[y][x+1]
    except IndexError:
        if verbose == 1:
            print(([y,x+1],'indexerror'))
        
    try:
        if x-1 >= 0:
            if verbose == 1:
                print(([y,x-1],matrix[y][x-1]))
            neighboors += matrix[y][x-1]
    except IndexError: 
        if verbose == 1:
            print(([y,x-1],'indexerror'))
        
    try:
        
        if verbose == 1:
            print(([y+1,x+1],matrix[y+1][x+1]))
        neighboors += matrix[y+1][x+1]
    except IndexError:
        if verbose == 1:
            print(([y+1,x+1],'indexerror'))
        
    try:
        if x-1 >= 0:
            if verbose == 1:
                print(([y+1,x-1],matrix[y+1][x-1]))
            neighboors += matrix[y+1][x-1]
    except IndexError:
        if verbose == 1:
            print(([y+1,x-1],'indexerror'))
        
    try:
        if y-1 >= 0:
            if verbose == 1:
                print(([y-1,x+1],matrix[y-1][x+1]))
            neighboors += matrix[y-1][x+1]
    except IndexError: 
        if verbose == 1:
            print(([y-1,x+1],'indexerror'))
        
    try:
        if y-1 >= 0 and x-1 >= 0:
            if verbose == 1:
                print(([y-1,x-1],matrix[y-1][x-1]))
            neighboors += matrix[y-1][x-1]
    except IndexError:
        if verbose == 1:
            print(([y-1,x-1],'indexerror'))
        
    try:
        if verbose == 1:
            print(([y+1,x],matrix[y+1][x]))
        neighboors += matrix[y+1][x] 
    except IndexError: 
        if verbose == 1:
            print(([y+1,x],'indexerror'))
        
    try:
        if y-1 >= 0:
            if verbose == 1:
                print(([y-1,x],matrix[y-1][x]))
            neighboors += matrix[y-1][x]
    except IndexError:
        if verbose == 1:
            print(([y-1,x],'indexerror'))
        
    return(neighboors)


import matplotlib.pylab as pl

nx = space.shape[0]
ny = space.shape[1]

def fDisplay(matrix):
    pl.figure()
    tb = pl.table(cellText=matrix, loc=(0,0), cellLoc='center')
    
    tc = tb.properties()['child_artists']
    for cell in tc: 
        cell.set_height(1/ny)
        cell.set_width(1/nx)
    
    ax = pl.gca()
    ax.set_xticks([])
    ax.set_yticks([])
    plt.show()
    return()

#space[5][4]
#space[5][3]
#space[5][5]
#fNeighcount(space_start,4,6,1)

step = 0
lSpacetime = []
sInput = ''
space3 = np.zeros(shape=(space.shape[0],space.shape[1]))
while sInput != 'n':
    lSpacetime.append(copy.deepcopy(space))
    sInput = input('Press enter to continue, type n to exit...' + str(step))
    if sInput == 'n':
        break
    step += 1 
    space2 = copy.deepcopy(space)
    #space3 = np.zeros(shape=(space.shape[0],space.shape[1]))
    for x in range(space.shape[1]):
        #print('x axis: '+str(x))
        for y in range(space.shape[0]):
            n = fNeighcount(space,y,x)
            #print('coordinates: '+ str((y,x)) + ',alive: ' + str(space[y][x] == 1) + ' ,neighboors: ' + str(n))
            if n == 3:
                space2[y][x] = 1
                space3[y][x] += 1
            if n < 2:    
                space2[y][x] = 0
#                space3[y][x] = 0
            if n > 3:    
                space2[y][x] = 0
#                space3[y][x] = 2
            
    space = copy.deepcopy(space2)
   
    fig = plt.figure()
    img2 = plt.imshow(space3, cmap='Greens', alpha = 0.65)
    img3 = plt.imshow(lSpacetime[-1], cmap='Greys', alpha = 0.8)
    plt.show()
    for i in lSpacetime:
        if np.array_equal(i, space):
            print('Cold state reached in steps...' + str(step))

            sInput = 'n'
            break
    #print('neigh_matrix_')
    #fDisplay(space3)
   # print('result:')
   # fDisplay(space)
plt.figure(figsize=(1.5,1.5))
plt.axis('off')
img2 = plt.imshow(space3, cmap='Greens', alpha = 0.8)
plt.show()




         
