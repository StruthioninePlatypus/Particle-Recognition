import math, numpy, re, pylab
from line import mkline
from sympy import *
from mech import dist, perimiter, split, colinear

def ittatpntceto(coords):
    x,y = split(coords)
    totx, toty = sum(x), sum(y)
    cenx, ceny = totx / len(x), toty / len(y)
    cent = (cenx, ceny) 
    sma = 256
    smack = None
    for i in coords:
        if dist(i,cent) < sma: 
            sma = dist(i,cent)
            smack = i
    neigh = 0
    for i in coords:
        if abs(dist(i,smack)-1.0) <=0.1:
            neigh += 1
    if neigh < 3:
        return True
    return False

class impact:
    
    def __init__(self, coords, number):
        self.coords = coords
        self.number = number
        # Calculating largest diameter
        diameter, start = 0,1                          
        for i in range(start, len(self.coords)):
            for j in range(start+1, len(self.coords)):
                if dist(self.coords[i],self.coords[j]) > diameter:
                    diameter,a,b = dist(self.coords[i],self.coords[j]),self.coords[i],self.coords[j]
                    start += 1
        self.bigline = mkline(a,b)                 
        self.bigdiam = diameter 
        # Calculating centroid
        x,y = split(self.coords)
        totx, toty = sum(x), sum(y)
        cenx, ceny = totx / len(x), toty / len(y)
        self.centroid =  (cenx, ceny) ###
        # Calculating smallest diameter through centroid
        diameter, start, per = 256,1,perimiter(self.coords)
        for i in range(start, len(per)):
            for j in range(start+1, len(per)):
                if i == j: continue
                if colinear(per[i],self.centroid,per[j]):
                    if dist(per[i],per[j]) < diameter: diameter = dist(per[i],per[j])
        self.smalldiam = diameter

    
    def shapecoef(self):
        # The closer shapecoef() is to 1, the more circular the blob
        return self.bigdiam / self.smalldiam
            
    def meanthick(self):
        # So far unused, not sure if useful
        thicktot = 0
        for i in perimiter(self.coords):
            thicktot += (self.bigline.dist2self(i))
        return thicktot /(0.5 * len(perimiter(self.coords)))
            
    def diffthick(self):
        # A diffthick() close to 0 means a fairly uniform thickness
        big, small = 0, 256
        for i in perimiter(self.coords):
            if i in self.bigline.extrms(): continue
            thick = self.bigline.dist2self(i)
            if thick > big: big = thick
            if thick < small: small = thick
        return big - small
            
    def curvature(self):      
        x,y = split(self.coords)
        coefs = numpy.polyfit(x,y,3)
        x = Symbol('x')
        poly = coefs[0]*(x**3) +coefs[1]*(x**2) + coefs[2]*x + coefs[3]
        diffy =  poly.diff(x).diff(x).diff(x)
        return abs(diffy)*100
        
    def analyse(self):     
        def exampletree():
            # This is an example of a branching algorithm.  The values used
            # here are fairly arbitrary.
            if self.shapecoef() < 2:
                if self.bigdiam < 3: tipo = 'gamma'
                elif not(ittatpntceto(self.coords)): tipo = 'alpha'
                else: tipo = 'beta'
            else:
                if self.curvature() < 0.1:
                    if self.diffthick() < 2: tipo = 'proton'
                    else: tipo = 'heavy ion'
                elif self.curvature()< 0.7: tipo = 'beta'
                else: tipo = 'beta'
            return tipo
        return exampletree()
        
    def showthyself(self):
        # Crude display for blob
        pylab.figure()
        x,y = split(self.coords)
        pylab.plot(x,y,'ks')
        cx,cy = self.centroid[0],self.centroid[1]
        pylab.plot(cx,cy,'ro')
        pylab.xlim([cx+40,cx-40])
        pylab.ylim([cy+40,cy-40])
        pylab.show()

def mkimpact(pts,no):
    return impact(pts,no)
