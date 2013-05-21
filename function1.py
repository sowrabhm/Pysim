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
#************************************************************************************************************************
def unicast(next,dst):
 cur=next
 if cur==dst:
    a=5
    #*print "Reached destination ",cur
 else:
    path=nx.dijkstra_path(G,cur,dst)
    
    for i in range(0,len(path)):
        #*print"Unicasting :Currently at node ",path[i]
        if i==len(path)-1:
           #*print "Reached destination ",path[i]
           a=5
        if i!=len(path)-1:
           wt=G.edge[cur][path[i+1]]['weight']
           H.add_edge(cur,path[i+1],weight=wt)
           #*print"Adding edge from ",cur," to ",path[i+1]
           global totalwt
           global hopcount        
           totalwt=totalwt+wt
           hopcount=hopcount+1
           #*print"Now hop count is =",hopcount
           cur=path[i+1]
           #*print"Next hop is ",path[i+1]



#************************************************************************************************************************
def function1(M,source,dstlist): 
 global G
 global H
 global totalwt
 global hopcount
 G=M
 totalwt=0
 hopcount=0
 H=nx.Graph()
 remdstlist=dstlist
 tremdstlist=remdstlist
 start=time.time()
 #*print "There no of destinations is ",len(dstlist),"and they are ",dstlist,"and source is ",source

 dstno=len(remdstlist)
 paths=[[] for i in range(dstno)]       # paths is a 2d list ,containing shortest path to every destination
 count=0
 for j in dstlist:
   paths[count]=nx.dijkstra_path(G,source,dstlist[count])
   #*print(paths[count])
   count=count+1
 table=paths
 flag=0                                   # flag to terminate outer loop when all destinations reached
 flag1=0                                  # flag to indicate split
 dstflag=0                                # flag to indicate one set of destinations is reached, got to next subset
 nextchkflag=0                            # flag to indicate if we already know nexthop 
 cur=paths[0][0]                          # cur=1
 table2temp=[]
 table2nexthop=[]
 table2cur=[]

 #**********************************************MAIN LOGIC ************************************************************
 while (flag<1): 
   flag1=0
   dstno=len(tremdstlist)
   if (dstflag==1 and len(table2cur)==0):
       flag=1
       break  
   if (len(table2cur)!=0 and dstflag==1):
       tremdstlist=table2temp.pop()
       cur=table2cur.pop()
       prednext=table2nexthop.pop()
       dstflag=0
       nextchkflag=1
   #*print "Currently at node             --->",cur
   #*print "Now delivering to destinations--->  ",tremdstlist
   for n in tremdstlist:
       if cur==n:
          #*print"Reached destination ",cur
          tremdstlist.remove(cur)    
   dstno=len(tremdstlist)
   if dstno==0:
           dstflag=1
           continue
   if (nextchkflag==0):
       paths=[[] for i in range(dstno)]       # paths is a 2d list ,containing shortest path to every destination
       count=0
       for j in tremdstlist:
           paths[count]=nx.dijkstra_path(G,cur,tremdstlist[count])
           #*print(paths[count])
           count=count+1                          # Outermost loop to run till all destinations reached
  
       nexthop=[]
       for i in range(dstno):                  # creating list of nexthops
            nexthop.append(paths[i][1])
       a=nexthop[0]
       for x in nexthop: 
           if x!=a:                            # checking if next hop is same for all
              flag1=1                         # if flag 1=1 means there is split


   if (nextchkflag==1):
       nextchkflag=0
       nexthop=[]
       nexthop.append(prednext)
   if flag1==0:                            # Condition of common next hop for all
       #*print "The next hop is ",nexthop[0],"for all destinations"
       #*print "Sending packet to nexthop",nexthop[0]  
      
       wt=G.edge[cur][nexthop[0]]['weight']
       H.add_edge(cur,nexthop[0],weight=wt)
       #*print "Adding edge from ",cur, " to",nexthop[0]
       totalwt=totalwt+wt
       hopcount=hopcount+1
       #*print "Now hopcount is ==", hopcount

       cur=nexthop[0]
      

   if flag1==1:
       #*print "Splitting packet ..........."
       table2=[]
       nexthop2=[]
       dstno=len(tremdstlist)
       nexthopcnt=0
      
       for i in range(dstno):
          
           if i==0:
             
              temp=[]
              temp.append(tremdstlist[0])
              table2.append(temp)
              nexthop2.append(nexthop[0])
              nexthopcnt=nexthopcnt+1
             
           if i>0:
             
              flag2=0 
             
              for k in range(0,nexthopcnt):
                 
                  if nexthop2[k]==nexthop[i]:
                     flag2=1
                    
                     location=k
              if flag2==0:
                  temp=[]
                  temp.append(tremdstlist[i])
                  table2.append(temp)
                  nexthop2.append(nexthop[i])
                  nexthopcnt=nexthopcnt+1
                 
              elif flag2==1:
                 
                  temp=tremdstlist[i]
                  table2[location].append(temp)
                 
       #*print"Table2 is ",table2
       #*print"nexthop2 is ",nexthop2
       copytable=copy.deepcopy(table2)
       copynexthop=list(nexthop2)
   #   print "nexthop2 is",nexthop2
      
       for i in range(nexthopcnt):
              #*print"the ",i,"th  set is ",table2[i],"and its length is ",len(table2[i])            
              if len(table2[i])==1:
                
                 #*print "One pkt copy sent to next hop ",nexthop2[i],"for the destination",table2[i][0]
                 #*print "Current node is ",cur
                 wt=G.edge[cur][nexthop2[i]]['weight']
                 H.add_edge(cur,nexthop2[i],weight=wt)
                 #*print "Adding edge from ",cur," to ",nexthop2[i]
                 unicast(nexthop2[i],table2[i][0])
                 totalwt=totalwt+wt
                 hopcount=hopcount+1
                 #*print "Now hopcount is ===", hopcount
                 #*print "Removing nexthop ",nexthop2[i],"and destination ",table2[i][0]
                 tremdstlist.remove(table2[i][0])
               
                 #*print "copynexthop is ",copynexthop,"when i is=",i  
                 copynexthop.remove(nexthop2[i])
                 #*print "copynexthop after pop is ",copynexthop
                 copytable.remove(table2[i])
                 #*print "now table2 is ",table2 ,"and nexthop2 is ",nexthop2
       if len(tremdstlist)==0:
             dstflag=1
             continue
       if len(copynexthop)!=0:
         pushcount=len(copynexthop)
         if (pushcount>1):
             for x in range (0,pushcount-1):
                 table2temp.append(copytable[x])
                 for k in range (0,len(copytable[x])):
                          tremdstlist.remove(copytable[x][k])
                 table2nexthop.append(nexthop[x])
                 table2cur.append(cur)
             nt=copynexthop[pushcount-1]
         else:
             nt=nexthop[1] 
         #*print "copynexthop is now ",copynexthop  
         wt=G.edge[cur][nt]['weight']
         H.add_edge(cur,nt,weight=wt)    
         #*print "Adding edge from ",cur, "to nexthop",nt
         totalwt=totalwt+wt
         hopcount=hopcount+1
         #*print "Now hopcount is ====", hopcount
         cur=nt
       
      

 #*print "**************** Total cost is ",totalwt,"***************"
 #*print "**************** Total hop count is ",hopcount,"***************"
 utility=float (hopcount)/G.number_of_edges()


 percent=utility*100
 #*print "***************Utilisation of the network is",percent," % ***************"
 end=time.time()
 runtime=end-start
 #*print 'Runtime is ',runtime
 #plt.figure(1)
 #nx.draw_graphviz(G,edge_color='r')
 #nx.draw_graphviz(G,edge_labels=dict, label_pos=0.5, font_size=10, font_color='k',edge_color='r')
 #nx.draw_networkx_edge_labels(G, pos=nx.graphviz_layout(G),edge_labels=dict, label_pos=0.5, font_size=10, font_color='k', font_family='sans-serif', font_weight='normal', alpha=0.9, bbox=None, ax=None, rotate=False)


 #plt.figure(2)
 #nx.draw_graphviz(H,edge_color='b')


 #plt.show()

 return (totalwt,runtime)
