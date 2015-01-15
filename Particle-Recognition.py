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
