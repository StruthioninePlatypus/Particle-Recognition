from math import sqrt, fabs

class line:
    
    def __init__(self,a,b):
        self.a = a
        self.b = b
        try:
            self.m = (self.b[1]-self.a[1])/(self.b[0]-self.a[0])
        except:
            if self.b[0] == self.a[0]: self.m = 0
            else: self.m = None
            # Need to code special case x = k
        self.c = self.a[1] - self.m *self.a[0]

    def ison(self,point):
        if point[1] == self.m*point[0] + self.c: return True
        return False
        
    def dist2self(self, p):
        ab = self.b[0]-self.a[0], self.b[1]-self.a[1]           
        mag = sqrt(ab[0]**2+ab[1]**2)         
        ab = ab[0]/mag, ab[1]/mag              
        n = -ab[1], ab[0]
        ac = p[0]-self.a[0], p[1]-self.a[1]          
        return fabs(ac[0]*n[0]+ac[1]*n[1]) 

def mkline(a,b):
    return line(a,b)
