# -*- coding: utf-8 -*-
import sys

def maze (inmaze):
    """Given laser maze dimensions, laser starting coords and direction, and mirror types/positions, return laser end coords and tiles traversed"""
    #read grid size and set up grid
    gridsize = [int(i) for i in inmaze.readline().split(' ')] 
    rows = gridsize[0]
    cols = gridsize[1]
    gridset = [[0 for i in range(cols)] for t in range(rows)]
    #create starting character variables
    startp = inmaze.readline().split(' ')
    startdir = str(startp.pop())
    startdir = startdir.rstrip()
    startp = [int(i) for i in startp]
    #populate grid with mirrors
    mirrorpos = 1
    while mirrorpos:
        mirrorpos = inmaze.readline().split(' ')
        mirrortype = str(mirrorpos.pop())
        mirrortype = mirrortype.rstrip()
        mirrorpos = [int(i) for i in mirrorpos]
        if len(mirrorpos) >1:
            mirx = mirrorpos[0]
            miry = mirrorpos[1]
            if mirrortype == '/':
                gridset[mirx][miry] = 4
            else:
                gridset[mirx][miry] = 5
    totalmoves=0
    currentmovingdir=0
    #move character and count moves
    #while conditions check if laser has left maze boundries
    while startp[0] < gridsize[0] and startp[1] < gridsize[1] and startp[0] > -1 and startp[1] > -1:
    #N=1, E=2, S=3, W=4
    #deal with initial starting position
        if startdir == 'S':
            startp[1] = startp[1]-1
            startdir=0
            currentmovingdir=3
            totalmoves += 1
        if startdir == 'N':
            startp[1] = startp[1]+1
            startdir=0
            currentmovingdir=1
            totalmoves += 1
            try:
                gridset[startp[0]][startp[1]]
            except IndexError:
                break
        if startdir == 'W':
            startp[0] = startp[0]-1
            startdir=0
            currentmovingdir=4
            totalmoves += 1
        if startdir == 'E':
            startp[0] = startp[0]+1
            startdir=0
            currentmovingdir=2
            totalmoves += 1
            try:
                gridset[startp[0]][startp[1]]
            except IndexError:
                break
    #going S
        if startdir == 0 and currentmovingdir == 3 and gridset[startp[0]][startp[1]] == 0:
            startp[1] = startp[1]-1
            totalmoves += 1
        if startdir == 0 and currentmovingdir == 3 and (gridset[startp[0]][startp[1]] == 4 or gridset[startp[0]][startp[1]] == 6 or gridset[startp[0]][startp[1]] == 7):
            if gridset[startp[0]][startp[1]] == 6:
                totalmoves = 0
                break
            gridset[startp[0]][startp[1]] = 6
            startp[0] = startp[0]-1
            currentmovingdir = 4
            totalmoves += 1
        if startdir == 0 and currentmovingdir == 3 and (gridset[startp[0]][startp[1]] == 5  or gridset[startp[0]][startp[1]] == 9 or gridset[startp[0]][startp[1]] == 8):
            if gridset[startp[0]][startp[1]] == 9:
                totalmoves = 0
                break
            gridset[startp[0]][startp[1]] = 9
            startp[0] = startp[0]+1
            currentmovingdir = 2
            totalmoves += 1
            try:
                gridset[startp[0]][startp[1]]
            except IndexError:
                break
    #going E
        if startdir == 0 and currentmovingdir == 2 and gridset[startp[0]][startp[1]] == 0:
            startp[0] = startp[0]+1
            totalmoves += 1
            try:
                gridset[startp[0]][startp[1]]
            except IndexError:
                break
        if startdir == 0 and currentmovingdir == 2 and (gridset[startp[0]][startp[1]] == 4  or gridset[startp[0]][startp[1]] == 6 or gridset[startp[0]][startp[1]] == 7):
            if gridset[startp[0]][startp[1]] == 6:
                totalmoves = 0
                break
            gridset[startp[0]][startp[1]] = 6
            startp[1] = startp[1]+1
            currentmovingdir = 1
            totalmoves += 1
            try:
                gridset[startp[0]][startp[1]]
            except IndexError:
                break
        if startdir == 0 and currentmovingdir == 2 and (gridset[startp[0]][startp[1]] == 5  or gridset[startp[0]][startp[1]] == 8 or gridset[startp[0]][startp[1]] == 9):
            if gridset[startp[0]][startp[1]] == 8:
                totalmoves = 0
                break
            gridset[startp[0]][startp[1]] = 8
            startp[1] = startp[1]-1
            currentmovingdir = 3
            totalmoves += 1
    #going W
        if startdir == 0 and currentmovingdir == 4 and gridset[startp[0]][startp[1]] == 0:
            startp[0] = startp[0]-1
            totalmoves += 1
        if startdir == 0 and currentmovingdir == 4 and (gridset[startp[0]][startp[1]] == 4  or gridset[startp[0]][startp[1]] == 7 or gridset[startp[0]][startp[1]] == 6):
            if gridset[startp[0]][startp[1]] == 7:
                totalmoves = 0
                break
            gridset[startp[0]][startp[1]] = 7
            startp[1] = startp[1]-1
            currentmovingdir = 3
            totalmoves += 1
            try:
                gridset[startp[0]][startp[1]]
            except IndexError:
                break
        if startdir == 0 and currentmovingdir == 4 and (gridset[startp[0]][startp[1]] == 5  or gridset[startp[0]][startp[1]] == 9 or gridset[startp[0]][startp[1]] == 8):
            if gridset[startp[0]][startp[1]] == 9:
                totalmoves = 0
                break
            gridset[startp[0]][startp[1]] = 9
            startp[1] = startp[1]+1
            currentmovingdir = 1
            totalmoves += 1
            try:
                gridset[startp[0]][startp[1]]
            except IndexError:
                break
    #going N
        if startdir == 0 and currentmovingdir == 1 and gridset[startp[0]][startp[1]] == 0:
            startp[1] = startp[1]+1
            totalmoves += 1
            try:
                gridset[startp[0]][startp[1]]
            except IndexError:
                break
        if startdir == 0 and currentmovingdir == 1 and (gridset[startp[0]][startp[1]] == 4  or gridset[startp[0]][startp[1]] == 7 or gridset[startp[0]][startp[1]] == 6):
            if gridset[startp[0]][startp[1]] == 7:
                totalmoves = 0
                break
            gridset[startp[0]][startp[1]] = 7
            startp[0] = startp[0]+1
            currentmovingdir = 2
            totalmoves += 1
            try:
                gridset[startp[0]][startp[1]]
            except IndexError:
                break
        if startdir == 0 and currentmovingdir == 1 and (gridset[startp[0]][startp[1]] == 5  or gridset[startp[0]][startp[1]] == 8 or gridset[startp[0]][startp[1]] == 9):
            if gridset[startp[0]][startp[1]] == 8:
                totalmoves = 0
                break
            gridset[startp[0]][startp[1]] = 8
            startp[0] = startp[0]-1
            currentmovingdir = 4
            totalmoves += 1
    #fix for overshooting of end point
    if currentmovingdir == 1:
        startp[1] -= 1
    if currentmovingdir == 2:
        startp[0] -= 1
    if currentmovingdir == 3:
        startp[1] += 1
    if currentmovingdir == 4:
        startp[0] += 1   
    # return results as a dictionary   
    return {'totalmnoves': totalmoves-1, 'startp':startp }
#code for input/output
if __name__ == '__main__':
     with open(sys.argv[2], 'w') as outfile:
        with open(sys.argv[1], 'r') as inmaze:
            result_dict = maze(inmaze)
            outfile.write(str(result_dict['totalmnoves']))
            outfile.write('\n')
            outfile.write(str(result_dict['startp'][0]))
            outfile.write(' ')
            outfile.write(str(result_dict['startp'][1]))
