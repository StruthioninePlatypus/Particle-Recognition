#'hub' for analysis

import math, numpy, pylab, re
from line import mkline
from sympy import *
from mech import dist, perimiter, split, colinear

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

    def analyse(self):
        def shapecoef():
            # The closer shapecoef() is to 1, the more circular the blob
            return self.bigdiam / self.smalldiam
        def meanthick():
            # So far unused, not sure if useful
            thicktot = 0
            for i in perimiter(self.coords):
                thicktot += (self.bigline.dist2self(i))
            return thicktot /(0.5 * len(perimiter(self.coords)))
        def diffthick():
            # A diffthick() close to 0 means a fairly uniform thickness
            big, small = 0, 256
            for i in perimiter(self.coords):
                if i in self.bigline.extrms(): continue
                thick = self.bigline.dist2self(i)
                if thick > big: big = thick
                if thick < small: small = thick
            return big - small
        def curvature():      
            x,y = split(self.coords)
            coefs = numpy.polyfit(x,y,3)
            x = Symbol('x')
            poly = coefs[0]*(x**3) +coefs[1]*(x**2) + coefs[2]*x + coefs[3]
            diffy =  poly.diff(x).diff(x).diff(x)
            return abs(diffy)*100
            
        def exampletree():
            # This is an example of a branching algorithm.  The values used
            # here are fairly arbitrary.
            if shapecoef() < 2:
                if self.bigdiam < 3: tipo = 'small dot'
                else: tipo = 'large dot'
            else:
                if curvature() < 0.1:
                    if diffthick() < 2: tipo = 'straight, even'
                    else: tipo = 'straight, comet'
                elif curvature()< 0.5: tipo = 'curved'
                else: tipo = 'very curved'
            return tipo
        return exampletree()

class frame:
    
    def __init__(self, blobs):
        self.impacts, name = [], 1
        for i in blobs:
            self.impacts.append(impact(i, name))
            name += 1
            
    def classify(self):
        results = {}
        for i in self.impacts:
            results[i.number] = i.analyse()
        return results
