# class for metadata, needs work...        

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
        
    def frequency(self):
        # Crude frequency data - could be used for checking algorithm with Gaussian elimination later
        p,b,a,g,hi = 0,0,0,0,0
        dat = self.classify()
        for i in dat.keys():
            print dat[i]
            if dat[i] == 'proton': p += 1
            if dat[i] == 'alpha': a += 1
            if dat[i] == 'gamma': g += 1
            if dat[i] == 'beta': b += 1
            if dat[i] == 'heavy ion': hi += 1
        return a,b,g,hi,p

    def display(self):
        for i in self.impacts:
            i.showthyself()
