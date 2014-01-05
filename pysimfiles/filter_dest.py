import random
import os
import sys
import networkx as nx




G=nx.Graph()


data = []
dict={}
f = open('/home/sowrabh/Desktop/jellyfish_topo.data', 'r')
for line in f.readlines():
    vector = line.split()
    x1=int(vector[0])
    if len(vector)<3:
       break
    x2=int(vector[1])
    w=float(vector[2])
    G.add_node(x1)
    G.add_node(x2)
    G.add_edge(x1,x2,weight=w)
    t=(x1,x2)
    dict[t]=w


n=G.nodes()
node_list=list(n)
destinations=[]
for node in node_list:
     if len(G.neighbors(node))==1:
         destinations.append(node)
print "Available destinations are :",len(destinations)

print "Destination number is ",len(destinations)-200
r= random.sample(destinations,len(destinations)-200)
f=open("destinations.txt",'w')
for node in r:
   f.write(str(node) +"\n")
f.close() 

