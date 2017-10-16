import matplotlib.pyplot as plt
import numpy as np
import pickle

mylist = []
with open("loss.txt","rb") as f:
    mylist = pickle.load(f)




def myp(mylist):
    x = []
    y = []
    
    i = 0
    for e,b,l in mylist:
        
        
        x.append(i)
        i += 1
        y.append(l)
        #print(f"e = {e}, b = {b}, l = {l}")
        
    plt.plot(x,y, 'ro')
    #plt.axis([0, 6, 0, 20])
    plt.savefig("loss.png")


def myp1(mylist):
    x = []
    y = []
    
    i = 0
    for l in mylist:
        
        
        x.append(i)
        i += 1
        y.append(l)
        #print(f"e = {e}, b = {b}, l = {l}")
        
    plt.plot(x,y, 'ro')
    #plt.axis([0, 6, 0, 20])
    plt.savefig("loss.png")



#print(mylist)
myp1(mylist)
