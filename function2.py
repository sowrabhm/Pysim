import math
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
prev_node=None
#************************************************************************************************************************



#************************************************************************************************************************
def unicast(G,next,dst):
 cur=next
 if cur==dst:
    #print "Reached destination ",cur
    a=5
 else:
    path=nx.dijkstra_path(G,cur,dst)
    
    for i in range(0,len(path)):
        #print"Unicasting :Currently at node ",path[i]
        if i==len(path)-1:
           #print "Reached destination ",path[i]
           a=5
        if i!=len(path)-1:
           wt=G.edge[cur][path[i+1]]['weight']
           H.add_edge(cur,path[i+1],weight=wt)
           #print"Adding edge from ",cur," to ",path[i+1]
           global totalwt
           global hopcount        
           totalwt=totalwt+wt
           hopcount=hopcount+1
           #*print"Now hop count is =",hopcount
           cur=path[i+1]
           #*print"Next hop is ",path[i+1]
def cost_split(G,cur,tremdstlist):
 
 csplit=0
 tablesplit=[[]  for i in range(len(tremdstlist))]
 num=0
 for j in tremdstlist:
    
     if (cur!=tremdstlist[num]):
           tablesplit[num]=nx.dijkstra_path(G,cur,tremdstlist[num])
     num=num+1
     
 #length=nx.all_pairs_dijkstra_path_length(G)
 csplit=nx.dijkstra_path_length(G,cur,tremdstlist[0])
 #print "CSPLIT added cost from :",cur, "to ",tremdstlist[0],"as ",length[cur][tremdstlist[0]]
 #*print "tablesplit[0]=",tablesplit[0]
 for x in range(1,num):
     curpath=tablesplit[x]
     
     for y in range(len(curpath)):
         if (y!=len(curpath)-1):
             
             if  ((curpath[y+1] in tablesplit[0]) !=True):
                 curwt=G.edge[curpath[y]][curpath[y+1]]['weight']
                 #print "CSPLIT : Adding [",curpath[y],"][",curpath[y+1],"]"
                 csplit=csplit+curwt
 return csplit

def cost_nsplit(G,cur,tremdstlist):
 #print "Entering cnsplit"
 alt_flag=0
 cnsplit=[]
 dest_grp=[]
 next=[]
 next2=[]
 targets=[]
 path_table=[]
 tremdstlist2=list(tremdstlist)
 tablensplit=[[]  for i in range(len(tremdstlist))]
 num=0

 for j in tremdstlist:
     present_flag=0
     tablensplit[num]=nx.dijkstra_path(G,cur,tremdstlist[num])
     #print "tablensplit[",num,"] is ",tablensplit[num]
     for next in next2:
        if tablensplit[num][1]==next:
             ptr=next2.index(next)
             present_flag=1
             dest_grp[ptr].append(j)
             index=0
             #print "Len of path table =",len(path_table[ptr])," len of tablensplit=",len(tablensplit[num])
             while path_table[ptr][index]==tablensplit[num][index]:
                   if index==len(path_table[ptr])-1 or index==len(tablensplit[num])-1:
                      break
                   else:
                       index=index+1
                   #print "Index=",index 
             path_table[ptr]=path_table[ptr][:index+1]
         
     #if (tablensplit[num][1] not in next2):
     if present_flag==0 and len(tablensplit[num])>2:
         next2.append(tablensplit[num][1])
         path_table.append(tablensplit[num])    
         temp=[]
         temp.append(j)
         dest_grp.append(temp)
     num=num+1

 # Filter 
 to_del=[]
 #*print 'Next2 is ',next2
 #*print 'tremdstlist is ',tremdstlist
 for i in next2:
     for j in tremdstlist:
         if i==j:
            continue
         path=nx.dijkstra_path(G,i,j)
         if cur in path:
              to_del.append(i)
         break

 for elem in to_del:
    next2.remove(elem)

 if (len(next2)!=0):
  for x in range(0,len(next2)):
     cost=G.edge[cur][next2[x]]['weight']+cost_split(G,next2[x],tremdstlist)
     cnsplit.append(cost)
  mincost=cnsplit[0]
  pos=0
  for y in range(0,len(next2)):
      if cnsplit[y]<mincost:
         mincost=cnsplit[y]
         pos=y
  cmin=mincost
  best_next=next2[pos]
  #print "Initial best_next and cmin are ",best_next," ",cmin
 else:
  cmin=99999
  best_next=0
  #*print '________________*******SINGLE PACKET NOT POSSIBLE*****_____________________'
 
 t_min=99999
 t_best_next=None
 use_flag=0
 
 if len(path_table)<=10 or len(tremdstlist)<=15 :
 #if use_flag==0:
   for i in range (len(path_table)-1):
      path=nx.dijkstra_path(G,path_table[i][-1],dest_grp[i+1][-1])
      best_target=path[1]
      target_cost=nx.dijkstra_path(G,path[1],path_table[i][-1])+nx.dijkstra_path(G,path[1],dest_grp[i+1][-1])
      for j in range (1,len(path)-1):
          if path[j] not in targets:
             cost=nx.dijkstra_path(G,path[j],path_table[i][-1])+nx.dijkstra_path(G,path[j],dest_grp[i+1][-1])
             if cost<target_cost:
                best_target=path[j]
                target_cost=cost 
      targets.append(best_target)
   for node in targets:
    #print "Scanning targets ...."
    if node!=cur: 
     cost=nx.dijkstra_path_length(G,cur,node)+cost_split(G,node,tremdstlist)
     if cost<t_min:
        t_min=cost
        t_best_next=nx.dijkstra_path(G,cur,node)[1]
   if t_min<cmin:
    #print "t_min= ",t_min ,"and c_min=",cmin
    use_flag=1
    cmin=t_min
    best_next=t_best_next
 result=[best_next,cmin,use_flag]
 return result 



#************************************************************************************************************************
#start=time.time()
def function2(G,source,dstlist):
 #global totalwt
 #global hopcount
 global H
 totalwt=0
 hopcount=0
 H=nx.Graph()
 
 #*print "\n  ______________________ SIMULATION TO DETERMINE MULTICAST PATH _________________________"
 #dstlist = raw_input("\n Enter destination list: ")
 #nodes=G.nodes()
 #dstlist=[]
 #r= random.sample(nodes, 64)
 #for i in r:
 #  dstlist.append(i)
 #s=1
 #if s in dstlist:
 #    dstlist.remove(s)

 #dstlist = map(int, dstlist.split())
 remdstlist=dstlist
 tremdstlist=remdstlist
 cost_dstlist=list(dstlist)
 start=time.time()

 #*print "There no of destinations is ",len(dstlist)

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
       prev_node=cur
       cur=table2cur.pop()
       if cur==prev_node:
           #print "Looping"
           pass
       prednext=table2nexthop.pop()
       dstflag=0
       nextchkflag=1
   #print "Currently at node             --->",cur
   #print "Now delivering to destinations--->  ",tremdstlist
   for n in tremdstlist:
       if cur==n:
          #print"Reached destination ",cur
          tremdstlist.remove(cur)    
   dstno=len(tremdstlist)
   if dstno==0:
           dstflag=1
           continue
   #if (nextchkflag==0):
   if len(tremdstlist)!=0:
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


   '''if (nextchkflag==1):
       nextchkflag=0
       nexthop=[]
       nexthop.append(prednext)'''
   if flag1==0:                            # Condition of common next hop for all
       #print "The next hop is ",nexthop[0],"for all destinations"
       #print "Sending packet to nexthop",nexthop[0]  
      
       wt=G.edge[cur][nexthop[0]]['weight']
       H.add_edge(cur,nexthop[0],weight=wt)
       #print "Adding edge from ",cur, " to",nexthop[0]
       totalwt=totalwt+wt
       hopcount=hopcount+1
       #print "Now hopcount is ==", hopcount
       prev_node=cur
       cur=nexthop[0]
       if cur==prev_node:
          #print "LOOPING"      
          pass
   if flag1==1:
       #print "Splitting packet ...........?"
       csplit=cost_split(G,cur,tremdstlist)
       #print "csplit cost  :  ",csplit
       result= cost_nsplit(G,cur,tremdstlist)
       cnsplit=result[1]
       if result[2]==1:
         #print "Cnsplit ==",cnsplit,"and csplit=",csplit
         #print "cnsplit cost : ",cnsplit
         pass
       if cnsplit<csplit:
            nt=result[0]   
            wt=G.edge[cur][nt]['weight']
            H.add_edge(cur,nt,weight=wt)
            prev_node=cur
            cur=nt
            continue
         
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
                 
       #print"Table2 is ",table2
       #print"nexthop2 is ",nexthop2
       copytable=copy.deepcopy(table2)
       copynexthop=list(nexthop2)
   #   print "nexthop2 is",nexthop2
      
       for i in range(nexthopcnt):
              #print"the ",i,"th  set is ",table2[i],"and its length is ",len(table2[i])            
              if len(table2[i])==1:
                
                 #print "One pkt copy sent to next hop ",nexthop2[i],"for the destination",table2[i][0]
                 #print "Current node is ",cur
                 wt=G.edge[cur][nexthop2[i]]['weight']
                 H.add_edge(cur,nexthop2[i],weight=wt)
                 #print "Adding edge from ",cur," to ",nexthop2[i]
                 unicast(G,nexthop2[i],table2[i][0])
                 totalwt=totalwt+wt
                 hopcount=hopcount+1
                 #print "Now hopcount is ===", hopcount
                 #print "Removing nexthop ",nexthop2[i],"and destination ",table2[i][0]
                 tremdstlist.remove(table2[i][0])
               
                 #print "copynexthop is ",copynexthop,"when i is=",i  
                 copynexthop.remove(nexthop2[i])
                 #print "copynexthop after pop is ",copynexthop
                 copytable.remove(table2[i])
                 #print "now table2 is ",table2 ,"and nexthop2 is ",nexthop2
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
         #print "copynexthop is now ",copynexthop  
         wt=G.edge[cur][nt]['weight']
         H.add_edge(cur,nt,weight=wt)    
         #print "Adding edge from ",cur, "to nexthop",nt
         totalwt=totalwt+wt
         hopcount=hopcount+1
         #print "Now hopcount is ====", hopcount
         prev_node=cur
         cur=nt
         
      
 mytotal=0
 for edge in H.edges():
    wt=H.edge[edge[0]][edge[1]]['weight']
    mytotal=mytotal+wt
 #print "**************** Total cost is ",mytotal,"***************"
 #print "**************** Total hop count is ",H.number_of_edges(),"***************"
 utility=float (hopcount)/G.number_of_edges() 


 percent=utility*100
 #print "***************Utilisation of the NWRk is",percent," % ***************"
 end=time.time()
 runtime=end-start
 #print 'Runtime is ',runtime
 plt.figure(1)
 nx.draw_graphviz(G,edge_color='r')


 plt.figure(2)
 nx.draw_graphviz(H,edge_color='b')
 costlist=[]
 sumcost=0
 for i in cost_dstlist:
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

 res=[mytotal,runtime,H.number_of_edges(),max,avg,median]
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
 #r= random.sample(nodes,48)
 #for i in range(65,140):
 #   dstlist.append(i)  # create destination list
 f = open('/home/sowrabh/Desktop/pysimfiles/destinations.txt', 'r')
 for line in f.readlines():
     dst=int(line.strip())
     dstlist.append(dst)
 source=dstlist[3]
 if source in dstlist:
  dstlist.remove(source)

 hopcount=function2(M,source,dstlist)
 

