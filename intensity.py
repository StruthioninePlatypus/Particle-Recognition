# These are some functions with pixel intensity integrated.  Each one takes a list of tupes of length 3,
# with the 3rd element the intensity, e.g. [(1,1,32),(2,3,13)]

from mech import *

def maxEnPt(pts):
    # Returns point(s) with highest intensity
    big = 0
    bigs = []
    for i in pts:
        if i[2]>big: big = i[2]
    for i in pts:
        if i[2]==big: bigs.append(i)
    return bigs

def weightedCentroid(pts):
    # Centroid weighted with intensity (uses centre of mass formula)
    x,y = split(pts)
    M,s = 0, [0,0]
    for i in range(len(pts)):
        M += pts[i][2]
        s[0] += pts[i][0]*pts[i][2]
        s[1] += pts[i][1]*pts[i][2]
    return ((1/M)*s[0],(1/M)*s[1])
    
def variation(pts):
    # Returns variation in intensity
    anyp,var = pts[0],0.0
    start = anyp[2]
    for i in range(1,len(pts)):
        var += abs(start-pts[i][2])
    return var
    
def meanEn(pts):
    # Returns average intensity of all points
    tot = 0
    for i in pts:
        tot += i[2]
    return tot/len(pts)
