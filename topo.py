import heapq
import os
import subprocess
from networkx.utils import generate_unique_node
import networkx as nx
from collections import defaultdict 
import networkx as nx

def create_topo():

 G=nx.Graph()
 G.add_edge(1,2,weight=2)
 G.add_edge(1,3,weight=5)
 G.add_edge(1,4,weight=2)
 G.add_edge(2,3,weight=1)
 G.add_edge(2,5,weight=1)
 G.add_edge(3,6,weight=1)
 G.add_edge(3,4,weight=2)
 G.add_edge(4,7,weight=1)
 G.add_edge(5,6,weight=1)
 G.add_edge(5,8,weight=1)
 G.add_edge(5,9,weight=1)
 G.add_edge(6,7,weight=1)
 G.add_edge(7,11,weight=1)
 G.add_edge(7,12,weight=2)
 G.add_edge(8,13,weight=4)
 G.add_edge(9,13,weight=2)
 G.add_edge(9,14,weight=2)
 G.add_edge(9,10,weight=1)
 G.add_edge(10,6,weight=1)
 G.add_edge(10,14,weight=2)
 G.add_edge(11,15,weight=2)
 G.add_edge(12,16,weight=3)
 G.add_edge(13,18,weight=1)
 G.add_edge(13,19,weight=2)
 G.add_edge(13,20,weight=1)
 G.add_edge(13,14,weight=4)
 G.add_edge(14,28,weight=1)
 G.add_edge(14,21,weight=2)
 G.add_edge(14,15,weight=1)
 G.add_edge(15,16,weight=1)
 G.add_edge(15,22,weight=3)
 G.add_edge(16,17,weight=2)
 G.add_edge(16,23,weight=3)
 G.add_edge(18,24,weight=4)
 G.add_edge(19,25,weight=2)
 G.add_edge(20,26,weight=1)
 G.add_edge(21,27,weight=3)
 G.add_edge(22,29,weight=2)
 G.add_edge(22,30,weight=2)
 G.add_edge(23,31,weight=1)
 '''G.add_edge(13,18,weight=1)
 G.add_edge(13,19,weight=1)
 G.add_edge(13,20,weight=1)
 G.add_edge(13,14,weight=1)
 G.add_edge(14,28,weight=3)
 G.add_edge(14,21,weight=2)'''


 return G

def create_toposmall():

  G=nx.Graph()
  G.add_edge(1,2,weight=1)
  G.add_edge(2,3,weight=1)
  G.add_edge(3,4,weight=1)
  G.add_edge(4,5,weight=1)
  G.add_edge(1,6,weight=1)
  G.add_edge(6,7,weight=1)
  G.add_edge(7,8,weight=1)
  G.add_edge(8,9,weight=1)
  G.add_edge(4,9,weight=5)
  
  return G


def create_topomed():
 G=nx.Graph()
 G.add_edge(1,2,weight=1)
 G.add_edge(2,3,weight=2)
 G.add_edge(2,4,weight=4)
 G.add_edge(2,5,weight=2)
 G.add_edge(3,4,weight=1)
 G.add_edge(4,5,weight=1)
 G.add_edge(3,6,weight=5)
 G.add_edge(4,7,weight=2)
 G.add_edge(5,8,weight=3)
 G.add_edge(6,7,weight=1)
 G.add_edge(7,8,weight=1)
 G.add_edge(6,9,weight=1)
 G.add_edge(7,10,weight=1)
 G.add_edge(8,11,weight=3)
 G.add_edge(8,12,weight=2)

 return G

def read_topo():

 G=nx.Graph()
 #os.chdir('/home/Downloads')
 
 data = []
 f = open('jellyfish_topo.data', 'r')
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

 return G 
