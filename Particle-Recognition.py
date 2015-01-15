from frame import *

def filereader(f):
    f,final = open(f),[]
    while True:
        try:
            b = eval(f.readline())
            final.append(b)
        except:
            break
    return final
    
def autoanalyse(rawfile):
    f = mkframe(filereader(rawfile))
    print f.frequency()
    
def deepanalyse(rawfile):
    f = mkframe(filereader(rawfile))
    print f.analyse()
    # Need to implement some sort of visual analysis output
    print f.frequency()
