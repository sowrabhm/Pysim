import random
import os
import sys
import networkx as nx
import pickle
def filter_dest(num):
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

 #print "Destination number is ",len(destinations)-num
 r= random.sample(destinations,180)
 rpoint=random.choice([x for x in (10,120) if  x not in r])
 pickle.dump(rpoint, open( "save.p", "wb" ) )
 os.chdir("/home/sowrabh/Desktop/pysimfiles")
 print "This is ",os.getcwd()
 f=open("destinations.txt",'w')
 for node in r:
   f.write(str(node) +"\n")
 f.close() 
 print "Written to file and closed !!"
if __name__ == "__main__":

 filter_dest(100)
