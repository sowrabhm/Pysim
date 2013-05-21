import time
import random
import algo1_function
import copy
import networkx as nx
import matplotlib.pyplot as plt
import topo
#***************************************************************************************************************************************
def recenter(i):
 a=list(table[i])
 #*print (a)
 b=[]
 for m in range(0,len(table[i])):
     b.append(0)
     for n in range(0,len(table[i])):
          #print 'Now m= ',m,'and n=',n         
          if (m!=n):
            short=nx.shortest_path(G,a[m],a[n],weight=None)
            b[m]=b[m]+len(short)-1    
 min=b[0]
 index=0
 for z in range(0,len(b)):
      #print 'Now min = ', min,'and b[z]= ',b[z]       
      if (b[z]<min):
            min=b[z]
            index=z
 #print 'Center of i changed from',center[i],'to',a[index],'and b=',b
 center[i]=a[index]
 
def adjust_path(source,dst,index):
 a=paths[index]
 #*print 'The path to be adjusted is ',a,'with destination',dst
 b=nx.shortest_path(G,source,target=dst)
 #print 'Finding vpoint for ',table[i][0],'and',table[i][1]
 #print 'paths are ',a,'and',b
 la=len(a)
 lb=len(b)
 if (la>lb): 
      short=lb
 else: 
      short=la
 ptr=0
 for x in range (0,short):
     #print 'a[x]=',a[x],'and b[x]=',b[x]                            
     if a[x]!=b[x]:
          ptr=x-1
          break
     if x==short-1:
          ptr=x
 cntr=a[ptr]
 vpoint[index]=cntr
 paths[index]=nx.shortest_path(G,source,target=cntr)
#***************************************************************************************************************************************
def function4(M,source,dstlist,limit):
 global G
 global H
 G=M
 start=time.time()
 
 #*print "\n  ______________________ SIMULATION TO DETERMINE MULTICAST PATH _________________________"
 #*print "SOURCE AT FUNCTION $ IS************** ",source
 grpcount=0
 global table
 global center
 global vpoint
 global paths
 table=[]
 center=[]
 vpoint=[]
 paths=[]
 for x in range(0,len(dstlist)):
   if (x==0):
      temp=[]
      temp.append(dstlist[x])
      table.append(temp)
      grpcount=grpcount+1
      center.append(dstlist[x])
      short=nx.shortest_path(G,source,dstlist[x])
      paths.append(short)    
      vpoint.append(dstlist[x])

   else:
      flag=0
      if dstlist[x] in paths :
         continue
      if dstlist[x] not in paths:
         for i  in range(0,len(table)):
              
                    shortest=nx.shortest_path(G,dstlist[x],target=center[i])
                    #print 'Shortest for source ',dstlist[x], 'and target ',center[i], 'is ',shortest
                    if (len(shortest)<=limit):
                        flag=1   
                        table[i].append(dstlist[x])
                        if len(table[i])>=2:
                          recenter(i)                     
              
                        if len(table[i])==2:
                          a=nx.shortest_path(G,source,target=table[i][0])
		          b=nx.shortest_path(G,source,target=table[i][1])
                          #print 'Finding vpoint for ',table[i][0],'and',table[i][1]
			  #print 'paths are ',a,'and',b
                          la=len(a)
                          lb=len(b)
                          if (la>lb): 
                             short=lb
                          else: 
                             short=la
                          ptr=0
                          for x in range (0,short):
                                #print 'a[x]=',a[x],'and b[x]=',b[x]                            
                                if a[x]!=b[x]:
                                   ptr=x-1
                                   break
                                if x==short-1:
                                   ptr=x
                          cntr=a[ptr]
                          vpoint[i]=cntr
                          paths[i]=nx.shortest_path(G,source,target=cntr)
		        if len(table[i])>=3:
                          a=paths[i]
		          b=nx.shortest_path(G,source,target=dstlist[x])
                          #print 'Finding vpoint for existing vpoint',vpoint[i],'and current dst',dstlist[x]
			  #print 'paths are ',a,'and',b
                          la=len(a)
                          lb=len(b)
                          if (la>lb): 
                             short=lb
                          else: 
                             short=la
                          ptr=0
                          for x in range (0,short):
                                #print 'a[x]=',a[x],'and b[x]=',b[x]                            
                                if a[x]!=b[x]:
                                   ptr=x-1
                                   break
                                if x==short-1:
                                   ptr=x
                          cntr=a[ptr]
                          vpoint[i]=cntr
                          paths[i]=nx.shortest_path(G,source,target=cntr)	
                        break
         if flag==0:
            t=dstlist[x]
            temp=[]
            temp.append(t)
            table.append(temp)
            grpcount=grpcount+1
            center.append(dstlist[x])
	    short=nx.shortest_path(G,source,dstlist[x])
            paths.append(short)
            vpoint.append(dstlist[x])

 #*print 'Before table ______: ',table
 #print 'Before paths =_____:',paths
 #*print 'Vpoint list is :',vpoint
 end_flag=0
 while(end_flag==0):
    for x in range(0,len(table)):
      #print 'x=',x,'and size of table =',len(table)
      #print 'current length is ',len(table[x])
      dist=[]
      pos=0
      if x==len(table)-1:
         end_flag=1
         break
      if len(table[x])==1:
         #*print 'Table is ',table
         #*print 'Single groupless destination {',table[x][0],'} found !!'
         for t in range(0,len(table)):
              if x!=t :
                #print 'x=',x,'and t=',t
                temp=[len(nx.shortest_path(G,table[x][0],target=vpoint[t],weight=None)),t]
                dist.append(temp)
         #*print 'dist =',dist
         min=dist[0][0]
     
         for z in range(0,len(dist)):
               if (dist[z][0]<=min):
                    #print 'Dist z is ',dist[z]
                    min=dist[z][0]
                    pos=dist[z][1]
                    #print 'Min has been set to ',min,'and pos set to ',pos  
         #print "min is ",min,'and pos =',pos
         table[pos].append(table[x][0])
         #*print 'Now table is ',table
         recenter(pos)
         adjust_path(source,table[x][0],pos)
         if x==len(table)-1:
                  end_flag=1
         table.remove(table[x])
         vpoint.pop(x)
         paths.pop(x)
         center.pop(x)    
         break
 #*print 'New vpoint list is ',vpoint
 #*print 'After table _____: ',table
 #*print 'The vpoint list is :',vpoint
 for x in range(0,len(vpoint)):
    if vpoint[x]==source:
         vpoint[x]=center[x]
         #table[x].remove(center[x])
 for x in range (0,len(vpoint)):
     if vpoint[x] in table[x]:
         table[x].remove(vpoint[x]) 
 #*print '____FINAL TABLE ___:',table,"__and vpoint__:",vpoint
 #print 'The center point  list is :',center
 #print 'The paths are ',paths
 #plt.figure(1)
 #nx.graphviz_layout(G,args='-Eweight=4')
 cost=0
 hopcount=0
 #nx.draw_graphviz(G,edge_labels=dict, label_pos=0.5, font_size=10, font_color='k',edge_color='r')
 #nx.draw_networkx_edge_labels(G, pos=nx.graphviz_layout(G),edge_labels=dict, label_pos=0.5, font_size=10, font_color='k', font_family='sans-  serif', font_weight='normal', alpha=1.0, bbox=None, ax=None, rotate=True)
 #plt.show()
 vpoint_copy=list(vpoint)
 H=nx.Graph()
 res=algo1_function.algo1_function(G,H,source,vpoint)
 H=res[0]
 cost=res[1]
 hopcount=res[2]
 #print (H.edges()) 
 x=0
 for v in vpoint_copy:
  if len(table[x])!=0:
     res=algo1_function.algo1_function(G,H,v,table[x])
     H=res[0]
     cost=cost+res[1]
     hopcount=hopcount+res[2]
  x=x+1
 end=time.time()
 runtime=end-start
 #*print 'Cost =',cost,'and hopcount =',hopcount 
 #plt.figure(2)
 #nx.draw_graphviz(H,edge_labels=dict, label_pos=0.5, font_size=10, font_color='k',edge_color='g')
 #plt.show()
 
 res=[cost,runtime]
 return res

