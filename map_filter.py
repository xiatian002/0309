#! -*- coding:utf-8 -*-
import os,time

now = lambda : time.time()
def checklist(x):
    if x >5:
        return x**2
num_list=[1,2,3,4,5,6,7,8,9,10,11,12,13]
#ma1=map(checklist,num_list)
fi1=filter(checklist,num_list)
print(list(fi1))
#print(now)