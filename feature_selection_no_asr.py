__author__ = 'zhouyu'
#!/usr/bin/env python

import pickle as pkl
import os
for split in ['train','val','test']:
    with open(os.path.join('data_clean', split) + '.pkl') as f:
        key = pkl.load(f)
        data = pkl.load(f)
        r1 = pkl.load(f)
        r2 = pkl.load(f)
    id = [8,85,86,87,88,89,90]
    data_select = data[:,id[:]]
    with open(os.path.join('data_clean_no_asr',split) +'.pkl','wb') as f:
        pkl.dump(key,f)
        pkl.dump(data_select,f)
        pkl.dump(r1,f)
        pkl.dump(r2,f)

