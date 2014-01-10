import random
import time
import copy
import networkx as nx
import matplotlib.pyplot as plt
#import testfunction
import topo
global totalwt
global hopcount
totalwt=0
hopcount=0


def functiongpim(M,source,dstlist,rpoint):
 #print "Source is ",source
 #print "DStlist is ", dstlist
 global totalwt
 global hopcount
 global G
 global H
 G=M
 totalwt=0
 hopcount=0
 H=nx.Graph()
 start=time.time()
 #rpoint=1
 dstlistcopy=list(dstlist)
 first=dstlistcopy[len(dstlistcopy)-1]
 path=nx.dijkstra_path(G,first,rpoint)
 member=[]
 member.append(rpoint)
 for i in range(len(path)):
   if i !=len(path)-1: 
    cur=path[i]
    next=path[i+1]
    wt=G.edge[cur][path[i+1]]['weight']
    H.add_edge(cur,path[i+1],weight=wt)
    member.append(cur)
    totalwt=totalwt+wt
    hopcount=hopcount+1
 dstlistcopy.pop()
 #print " Now dstlist is ",dstlistcopy
 for node in dstlistcopy:
       tempmember=[]
       #print "This node is ", node
       if node in member:
          #print "This node already in graph, so skip "
          continue
       else:
          path=nx.dijkstra_path(G,node,rpoint)
          #print "PAth is ", path
          for i in range(len(path)-1):
                  cur=path[i]
                  next=path[i+1]
                  if i==0:
                     tempmember.append(cur)
                  tempmember.append(next)   
                  #print "Cur is ",cur , "and next is ",next
                  
                  if cur in member:
                         #print "Cur is already in H and nodes of H are ",member
                         tempmember.remove(cur)
                         tempmember.remove(next)
                         if len(tempmember)!=0:
                            for node in tempmember:
                                 member.append(node)
                         break
                  else:  
                         #print "Adding edge ",cur ,"--",next
                         wt=G.edge[cur][next]['weight']
                         H.add_edge(cur,next,weight=wt)
                         totalwt=totalwt+wt
                         hopcount=hopcount+1
                         tempmember.append(cur)
                         if i==len(path)-2:
                            for node in tempmember:
                                  member.append(node)
 
            
 plt.figure(1)
 nx.draw_graphviz(G,edge_color='r')
 plt.figure(2)
 nx.draw_graphviz(H,edge_color='b')
 #plt.show()
 smember=[]
 stempmember=[]
 #print "Total wt is ", totalwt,"and hopcount is ",hopcount 
 if source!=rpoint:
     path=nx.dijkstra_path(G,source,rpoint)
     for i in range(len(path)-1):
                  cur=path[i]
                  next=path[i+1]
                  if i==0:
                     stempmember.append(cur)
                  stempmember.append(next)
                  #print "Cur is ",cur , "and next is ",next

                  if cur in smember:
                         #print "Cur is already in H and nodes of H are ",member
                         stempmember.remove(cur)
                         stempmember.remove(next)
                         if len(stempmember)!=0:
                            for node in stempmember:
                                 smember.append(node)
                         break
                  else:
                         #print "Adding edge ",cur ,"--",next
                         wt=G.edge[cur][next]['weight']
                         H.add_edge(cur,next,weight=wt)
                         totalwt=totalwt+wt
                         hopcount=hopcount+1
                         #print "Total wt is ", totalwt,"and hopcount is ",hopcount

                         if i==len(path)-2:
                            for node in stempmember:
                                  smember.append(node)

 end=time.time()
 runtime=end-start
 costlist=[]
 sumcost=0
 for i in dstlist:
    x=nx.dijkstra_path_length(H,source,i)
    sumcost=sumcost+x
    costlist.append(x)

 costlist.sort()
 max=costlist[len(costlist)-1]
 avg=float (sumcost)/len(costlist)
 median=0
 if len(costlist)%2 ==0:
    median_ptr=len(costlist)/2
    median=float(costlist[median_ptr]+costlist[median_ptr+1])/2

 else:
    median_ptr=(len(costlist)+1)/2
    median=float(costlist[median_ptr])
 mytotal=0
 for edge in H.edges():
    wt=H.edge[edge[0]][edge[1]]['weight']
    mytotal=mytotal+wt
 res=[totalwt,runtime,hopcount,max,avg,median]
 #print "****************GPIM Total cost is ",mytotal+nx.dijkstra_path_length(G,source,rpoint),"***************"
 #print "****************GPIM Total hop count is ",len(H.edges())+len(nx.dijkstra_path(G,source,rpoint))-1,"***************"
 #print"^^^^^^^^^^^^^^^^^ path is  ",nx.dijkstra_path(G,source,rpoint),"^^^^^^^^^^"
 res=[mytotal,runtime,hopcount,max,avg,median]
 #plt.show()
 return (res)

if __name__ == "__main__":
 M=nx.Graph()
 data = []
 f = open('jellyfish_topo.data', 'r')
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
 '''#r= random.sample(nodes,48)
 for i in range(1,45):
    dstlist.append(i)  # create destination list'''
 

 f = open('/home/sowrabh/Desktop/pysimfiles/destinations.txt', 'r')
 for line in f.readlines():
     dst=int(line.strip())
     dstlist.append(dst)
 source=dstlist[10]
 if source in dstlist:
  dstlist.remove(source)


 hopcount=functiongpim(M,source,dstlist)
 #print "Hopcount = ",hopcount[2]

