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
    # Need to implement some sort of visual analysis output
    for i in f.impacts:
        print i.analyse()

f = raw_input('Enter file path >>> ')
d = raw_input('Deep analysis? y or n >>> ')
if d == 'y':
    deepanalyse(f)
else:
    autoanalyse(f)
