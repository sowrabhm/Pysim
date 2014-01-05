import random
import time
import copy
import networkx as nx

import sys
sys.path.append('/home/sowrabh/Desktop')
from function2fast import function2fast
from functionpim import functionpim
from functiongpim import functiongpim

M=nx.Graph()
data = []
f = open('/home/sowrabh/Desktop/jellyfish_topo.data', 'r')
for line in f.readlines():
    vector = line.split()
    x1=int(vector[0])
    if len(vector)<3:
       break
    x2=int(vector[1])
    w=float(vector[2])
    M.add_node(x1)
    M.add_node(x2)
    M.add_edge(x1,x2,weight=w)

nodes=M.nodes()
dstlist=[]
#r= random.sample(nodes,43)

for i in range(1,45):
    dstlist.append(i)  # create destination list
source=1
if source in dstlist:
 dstlist.remove(source)
dstlist2=list(dstlist)
dstlist3=list(dstlist)
hopcount2=function2fast(M,49,dstlist2)
print "____________________________________________________________________________________ "
hopcount1=functiongpim(M,49,dstlist)
print "_____________________________________________________________________________________"
hopcount3=functionpim(M,49,dstlist3)
