import math

def dist(i,j):
    #distance between i and j
    return math.hypot(j[0]-i[0],j[1]-i[1])
    
def split(coords):
    #returns two lists of x and y coords
    x,y = [],[]
    for i in coords:
        x.append(i[0])
        y.append(i[1])
    return x,y

def colinear(p,q,r):
    #returns True iff p,q,r are colinear
    if abs((dist(p,q) + dist(q,r)) - dist(p,r)) < 0.00000001: return True
    return False
    
def perimiter(coords):
    #returns list of points on perimiter of coords
    perim, start = [],0
    for i in range(start, len(coords)):
        neighbours = 0
        for j in range(start+1, len(coords)):
            if coords[i] == coords[j]: continue
            if dist(coords[i],coords[j]) == 1: neighbours += 1
        if neighbours < 4: perim.append((coords[i]))
    return perim
