# class for metadata, needs work...    

from impact import *

class frame:
    
    def __init__(self, blobs):
        self.impacts, name = [], 1
        for i in blobs:
            self.impacts.append(mkimpact(i, name))
            name += 1
            
    def classify(self):
        results = {}
        for i in self.impacts:
            results[i.number] = i.analyse()
        return results
        
    def frequency(self):
        # Crude frequency data - could be used for checking algorithm with Gaussian elimination later
        p,b,a,g,h = 0,0,0,0,0
        dat = self.classify()
        for i in dat.keys():
            print dat[i]
            if dat[i] == 'proton': p += 1
            if dat[i] == 'alpha': a += 1
            if dat[i] == 'gamma': g += 1
            if dat[i] == 'beta': b += 1
            if dat[i] == 'heavy ion': h += 1
        frtot = len(self.impacts)
        print 'There are', frtot, 'blobs in the frame'
        print round(g/frtot,2), 'are gamma particles'
        print round(h/frtot,2), 'are heavy ions'
        print round(p/frtot,2), 'are protons'
        print round(b/frtot,2), 'are beta particles'
        print round(a/frtot,2), 'are alpha particles'

    def display(self):
        for i in self.impacts:
            i.showthyself()
