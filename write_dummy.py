# write a dummy loss curve

import numpy as np
import pickle



epoch = np.arange(30)
batch = np.arange(40)
loss = np.arange(10.,0.,-10./(30*40))
loss_list = []

for e in epoch:
    for b in batch:
        elem = [e+1,b+1, loss[e*epoch.size+b]]
        loss_list.append(elem)

#print(loss_list)
	with open('loss_dummy.pkl','wb') as f:
    pickle.dump(loss_list,f)
