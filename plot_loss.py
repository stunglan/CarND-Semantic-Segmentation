import matplotlib.pyplot as plt
import numpy as np
import pickle
import sys
import os.path

if len(sys.argv) < 2:
    print("provide filename")
    exit()

if not os.path.isfile(sys.argv[1]):
    print(f"Cannot find file {sys.argv[1]}")
    exit()

pfn = os.path.splitext(sys.argv[1])[0] + ".png"

print(pfn)

mylist = []
with open(sys.argv[1],"rb") as f:
    mylist = pickle.load(f)

def myp(mylist):
    x = []
    y = []

    ax = plt.gca()

    esize = np.array(mylist)
    esize = int(np.amax(esize[:,0]))
    bsize = np.array(mylist)
    bsize = int(np.amax(bsize[:,1]))
    
    xtl = np.arange(1,esize+1,1)
    xt = (xtl-1) * (bsize)
    
    i = 0
    for e,b,l in mylist:
        
        
        x.append(i)
        i += 1
        y.append(l)
        print(f"e = {e}, b = {b}, l = {l}")
        
    plt.plot(x,y,ls='solid')
    ax.set_xticks(xt)
    ax.set_xticklabels(xtl)

    for tick in ax.xaxis.get_major_ticks():
        tick.label.set_fontsize('x-small') 
    for tick in ax.yaxis.get_major_ticks():
        tick.label.set_fontsize('x-small') 


    ax.set_xlabel('epoch')
    ax.set_ylabel('loss')
    plt.savefig(pfn)


myp(mylist)

