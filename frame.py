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
        p,b,a,g,h = 0.0,0.0,0.0,0.0,0.0
        dat = self.classify()
        for i in dat.keys():
            if dat[i] == 'proton': p += 1.0
            if dat[i] == 'alpha': a += 1.0
            if dat[i] == 'gamma': g += 1.0
            if dat[i] == 'beta': b += 1.0
            if dat[i] == 'heavy ion': h += 1.0
        frtot = float(len(self.impacts))
        print 'There are', frtot, 'blobs in the frame\n'
        print round(g/frtot,2)*100, '% are gamma particles'
        print round(h/frtot,2)*100, '% are heavy ions'
        print round(p/frtot,2)*100, '% are protons'
        print round(b/frtot,2)*100, '% are beta particles'
        print round(a/frtot,2)*100, '% are alpha particles'

    def display(self):
        for i in self.impacts:
            i.showthyself()
            
def mkframe(bs):
    return frame(bs)
