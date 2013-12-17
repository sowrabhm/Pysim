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



#************************************************************************************************************************
def unicast(G,next,dst):
 cur=next
 if cur==dst:
    print "Reached destination ",cur
    a=5
 else:
    path=nx.dijkstra_path(G,cur,dst)
    
    for i in xrange(0,len(path)):
        print"Unicasting :Currently at node ",path[i]
        if i==len(path)-1:
           print "Reached destination ",path[i]
           a=5
        if i!=len(path)-1:
           wt=G.edge[cur][path[i+1]]['weight']
           H.add_edge(cur,path[i+1],weight=wt)
           print"Adding edge from ",cur," to ",path[i+1]
           global totalwt
           global hopcount        
           totalwt=totalwt+wt
           hopcount=hopcount+1
           print"Now hop count is =",hopcount
           cur=path[i+1]
           print"Next hop is ",path[i+1]
def cost_split(G,cur,tremdstlist):
 
 csplit=0
 tablesplit=[[]  for i in xrange(len(tremdstlist))]
 num=0
 for j in tremdstlist:
    
     if (cur!=tremdstlist[num]):
           tablesplit[num]=nx.dijkstra_path(G,cur,tremdstlist[num])
     num=num+1
     
 
 csplit=nx.dijkstra_path_length(G,cur,tremdstlist[0])
 #print "CSPLIT added cost from :",cur, "to ",tremdstlist[0],"as ",length[cur][tremdstlist[0]]
 #*print "tablesplit[0]=",tablesplit[0]
 for x in xrange(1,num):
     curpath=tablesplit[x]
     
     for y in xrange(len(curpath)):
         if (y!=len(curpath)-1):
             
             if  ((curpath[y+1] in tablesplit[0]) !=True):
                 curwt=G.edge[curpath[y]][curpath[y+1]]['weight']
                 #print "CSPLIT : Adding [",curpath[y],"][",curpath[y+1],"]"
                 csplit=csplit+curwt
 return csplit

def cost_nsplit(G,cur,tremdstlist):
 #*print "Entering cnsplit"
 cnsplit=[]
 next=[]
 next2=[]
 tremdstlist2=list(tremdstlist)
 tablensplit=[[]  for i in xrange(len(tremdstlist))]
 max_len=0
 result=[]
 max_len_path_list=[]
 num=0
 for j in tremdstlist:
     tablensplit[num]=nx.dijkstra_path(G,cur,tremdstlist[num]) # make a list of all paths
     if (tablensplit[num][1] not in next2):
         next2.append(tablensplit[num][1])                   # make a list of unique next hops
     if len(tablensplit[num])>max_len:
         max_len=len(tablensplit[num])
	 max_len_path_list=[]
	 max_len_path_list.append(tablensplit[num])
     if len(tablensplit[num])==max_len:
	 max_len_path_list.append(tablensplit[num])	
     num=num+1
 
 back_flag=0
 for path in max_len_path_list:
    for j in tremdstlist:
       if path[1]!=j and cur in nx.dijkstra_path(G,path[1],j):
        back_flag=1
        break
    if back_flag==0:
       result=[path[1],G.edge[cur][path[1]]['weight']+cost_split(G,path[1],tremdstlist)]	
    break	
 # Filter
 if result==[]: 
     to_del=[]
     for i in next2: 			# Remove those next hops that would possibly send pkt back to cur node
         for j in tremdstlist:
             if i==j:
                continue
             path=nx.dijkstra_path(G,i,j)  # Ignoring those next hops that are end destinations
             if cur in path:
                  to_del.append(i)
             break

     for elem in to_del:
        next2.remove(elem)

     if (len(next2)!=0):      
       cmin=G.edge[cur][next2[0]]['weight']+cost_split(G,next2[0],tremdstlist)
       best_next=next2[0]
     else:
       cmin=99999
       best_next=0
     result=[best_next,cmin]
 return result 



#************************************************************************************************************************
#start=time.time()
def function2fast(G,source,dstlist):
 #global totalwt
 #global hopcount
 global H
 totalwt=0
 hopcount=0
 H=nx.Graph()
 
 print "\n  ______________________ SIMULATION TO DETERMINE MULTICAST PATH _________________________"
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
 paths=[[] for i in xrange(dstno)]       # paths is a 2d list ,containing shortest path to every destination
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
   print "Currently at node             --->",cur
   print "Now delivering to destinations--->  ",tremdstlist
   if cur==34 or tremdstlist==[107,109]:
      print "Nextchkflag is ",nextchkflag
   for n in tremdstlist:
       if cur==n:
          print"Reached destination ",cur
          tremdstlist.remove(cur)    
   dstno=len(tremdstlist)
   if dstno==0:
           dstflag=1
           continue
   #if (nextchkflag==0):
   if len(tremdstlist)!=0:
       paths=[[] for i in xrange(dstno)]       # paths is a 2d list ,containing shortest path to every destination
       count=0
       for j in tremdstlist:
           paths[count]=nx.dijkstra_path(G,cur,tremdstlist[count])
           if cur==34 or tremdstlist==[107,109]:  
            print "Path found is ",paths[count]
           count=count+1                          # Outermost loop to run till all destinations reached
  
       nexthop=[]
       for i in xrange(dstno):                  # creating list of nexthops
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
       print "The next hop is ",nexthop[0],"for all destinations"
       print "Sending packet to nexthop",nexthop[0]  
      
       wt=G.edge[cur][nexthop[0]]['weight']
       H.add_edge(cur,nexthop[0],weight=wt)
       print "Adding edge from ",cur, " to",nexthop[0]
       totalwt=totalwt+wt
       hopcount=hopcount+1
       print "Now hopcount is ==", hopcount

       cur=nexthop[0]
      
   if flag1==1:
       print "Splitting packet ...........?"
       csplit=cost_split(G,cur,tremdstlist)
       print "csplit cost  :  ",csplit
       result= cost_nsplit(G,cur,tremdstlist)
       cnsplit=result[1]
       print "cnsplit cost : ",cnsplit
       if cnsplit<=csplit:
            nt=result[0]   
            wt=G.edge[cur][nt]['weight']
            H.add_edge(cur,nt,weight=wt)
            cur=nt 
            continue
         
       table2=[]
       nexthop2=[]
       dstno=len(tremdstlist)
       nexthopcnt=0
      
       for i in xrange(dstno):
          
           if i==0:
             
              temp=[]
              temp.append(tremdstlist[0])
              table2.append(temp)
              nexthop2.append(nexthop[0])
              nexthopcnt=nexthopcnt+1
             
           if i>0:
             
              flag2=0 
             
              for k in xrange(0,nexthopcnt):
                 
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
                 
       print"Table2 is ",table2
       print"nexthop2 is ",nexthop2
       copytable=copy.deepcopy(table2)
       copynexthop=list(nexthop2)
   #   print "nexthop2 is",nexthop2
      
       for i in xrange(nexthopcnt):
              print"the ",i,"th  set is ",table2[i],"and its length is ",len(table2[i])            
              if len(table2[i])==1:
                
                 print "One pkt copy sent to next hop ",nexthop2[i],"for the destination",table2[i][0]
                 print "Current node is ",cur
                 wt=G.edge[cur][nexthop2[i]]['weight']
                 H.add_edge(cur,nexthop2[i],weight=wt)
                 print "Adding edge from ",cur," to ",nexthop2[i]
                 unicast(G,nexthop2[i],table2[i][0])
                 totalwt=totalwt+wt
                 hopcount=hopcount+1
                 print "Now hopcount is ===", hopcount
                 print "Removing nexthop ",nexthop2[i],"and destination ",table2[i][0]
                 tremdstlist.remove(table2[i][0])
               
                 print "copynexthop is ",copynexthop,"when i is=",i  
                 copynexthop.remove(nexthop2[i])
                 print "copynexthop after pop is ",copynexthop
                 copytable.remove(table2[i])
                 print "now table2 is ",table2 ,"and nexthop2 is ",nexthop2
       if len(tremdstlist)==0:
             dstflag=1
             continue
       if len(copynexthop)!=0:
         pushcount=len(copynexthop)
         if (pushcount>1):
             for x in xrange (0,pushcount-1):
                 table2temp.append(copytable[x])
                 for k in xrange (0,len(copytable[x])):
                          tremdstlist.remove(copytable[x][k])
                 table2nexthop.append(nexthop[x])
                 table2cur.append(cur)
             nt=copynexthop[pushcount-1]
         else:
             nt=nexthop[1] 
         print "copynexthop is now ",copynexthop  
         wt=G.edge[cur][nt]['weight']
         H.add_edge(cur,nt,weight=wt)    
         print "Adding edge from ",cur, "to nexthop",nt
         totalwt=totalwt+wt
         hopcount=hopcount+1
         print "Now hopcount is ====", hopcount
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


 #plt.figure(2)
 #nx.draw_graphviz(H,edge_color='b')
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
 
 mytotal=0
 for edge in H.edges():
    wt=H.edge[edge[0]][edge[1]]['weight']
    mytotal=mytotal+wt 
 res=[totalwt,runtime,hopcount,max,avg,median]
 print "**************** Total cost is ",mytotal,"***************"
 print "**************** Total hop count is ",H.number_of_edges(),"***************"
 print "*****************Total nodes are ",H.number_of_nodes(),"*************" 
 print "Runtime is :",runtime
 plt.figure(1)
 nx.draw_graphviz(G,edge_color='r')
 plt.figure(2)
 nx.draw_graphviz(H,edge_color='b')
 plt.show()

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
 source=1
 if source in dstlist:
  dstlist.remove(source)

 hopcount=function2fast(M,source,dstlist)
 #print "Hopcount = ",hopcount[2]

