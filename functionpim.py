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

def functionpim(M,source,dstlist):
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
 dstlistcopy=list(dstlist)
 first=dstlistcopy[len(dstlistcopy)-1]
 path=nx.dijkstra_path(G,first,source)
 member=[]
 member.append(source)
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
          path=nx.dijkstra_path(G,node,source)
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
                         if i==len(path)-2:
                            for node in tempmember:
                                  member.append(node)
 
            
 # plt.figure(1)
 #nx.draw_graphviz(G,edge_color='r')
 plt.figure(2)
 nx.draw_graphviz(H,edge_color='b')
 plt.show()
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

 res=[totalwt,runtime,hopcount,max,avg,median]
 #plt.show()
 return (res)
