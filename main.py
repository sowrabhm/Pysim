import function1
import function2
import function4
import function5
import topo
import random
import time
import copy
import networkx as nx
import matplotlib.pyplot as plt
import os
import subprocess
from subprocess import call

cost1=[]
cost2=[]
cost4=[]
cost5=[]
cost6=[]
runtime1=[]
runtime2=[]
runtime4=[]
runtime5=[]
runtime6=[]
hop1=[]
hop2=[]
hop4=[]
hop5=[]
hop6=[]

subprocess.call(['./hello.sh'])

for i in range(0,8):
 
  
  G=topo.read_topo()   # Get topology from read function
  nodes=G.nodes()      
  dstlist=[]
  r= random.sample(nodes,32)
  for i in r:
    dstlist.append(i)  # create destination list

  s=random.sample(nodes,1)
  source=s[0]
  if source in dstlist:
    s=random.sample(nodes,1)    # select source
  source=s[0]
  if source in dstlist:
     dstlist.remove(source)
  dstlist2=list(dstlist)
  dstlist3=list(dstlist)
  dstlist4=list(dstlist)
  dstlist5=list(dstlist)
  res1=function1.function1(G,source,dstlist)
  cost1.append(res1[0])
  runtime1.append(res1[1])
  hop1.append(res1[2])
  res2=function2.function2(G,source,dstlist2)
  cost2.append(res2[0])
  runtime2.append(res2[1])
  hop2.append(res2[2])
  res4=function4.function4(G,source,dstlist3,5)
  cost4.append(res4[0])
  runtime4.append(res4[1])
  hop4.append(res4[2])
  res5=function5.function5(G,source,dstlist4,5)
  cost5.append(res5[0])
  runtime5.append(res5[1])
  hop5.append(res5[2])
  res6=function4.function4(G,source,dstlist5,8)
  cost6.append(res6[0])
  runtime6.append(res6[1])
  hop6.append(res6[2])
for i in range(0,len(cost1)):
 #print " ",cost1[i],"|",cost2[i],"|",cost4[i],"|",cost5[i],"|",cost6[i],"|",runtime1[i],"|",runtime2[i],"|",runtime4[i],"|",runtime5[i],"|",runtime6[i]
 print " ", hop1[i], " | ", hop2[i], " | ", hop4[i], " | ", hop5[i], " | ", hop6[i], " | "
#print (runtime1)
#print "___________________________________________________________________________________________________________________________________"
#print (cost2)
#print (runtime2)
#print "___________________________________________________________________________________________________________________________________"
#print (cost4)
#print (runtime4)

sumcost1=0
sumcost2=0
sumcost4=0
sumcost5=0
sumcost6=0

sumrtime1=0
sumrtime2=0
sumrtime4=0
sumrtime5=0
sumrtime6=0

sumhop1=0
sumhop2=0
sumhop4=0
sumhop5=0
sumhop6=0

for i in range(0,len(cost1)):
 sumcost1=sumcost1+cost1[i]
 sumcost2=sumcost2+cost2[i]
 sumcost4=sumcost4+cost4[i]
 sumcost5=sumcost5+cost5[i]
 sumcost6=sumcost6+cost6[i]
 
 sumrtime1=sumrtime1+runtime1[i]
 sumrtime2=sumrtime2+runtime2[i]
 sumrtime4=sumrtime4+runtime4[i]
 sumrtime5=sumrtime5+runtime5[i]
 sumrtime6=sumrtime6+runtime6[i]

 sumhop1=sumhop1+hop1[i]
 sumhop2=sumhop2+hop2[i]
 sumhop4=sumhop4+hop4[i]
 sumhop5=sumhop5+hop5[i]
 sumhop6=sumhop6+hop6[i]

avcost1=sumcost1/len(cost1)
avcost2=sumcost2/len(cost1) 
avcost4=sumcost4/len(cost1)
avcost5=sumcost5/len(cost1)
avcost6=sumcost6/len(cost1)

avrtime1=sumrtime1/len(runtime1)
avrtime2=sumrtime2/len(runtime1)
avrtime4=sumrtime4/len(runtime1)
avrtime5=sumrtime5/len(runtime1)
avrtime6=sumrtime6/len(runtime1)

avhop1=float (sumhop1)/len(hop1)
avhop2=float (sumhop2)/len(hop1)
avhop4=float (sumhop4)/len(hop1)
avhop5=float (sumhop5)/len(hop1)
avhop6=float (sumhop6)/len(hop1)



print 'Average cost1 : =',avcost1
print 'Average cost2 : =',avcost2
print 'Average cost4 : =',avcost4
print 'Average cost5 : =',avcost5
print 'Average cost6 : =',avcost6

print 'Average runtime 1 : = ',avrtime1
print 'Average runtime 2 : = ',avrtime2
print 'Average runtime 4 : = ',avrtime4
print 'Average runtime 5 : = ',avrtime5
print 'Average runtime 6 : = ',avrtime6


print 'Average net util 1 : = ',avhop1
print 'Average net util 2 : = ',avhop2
print 'Average net util 4 : = ',avhop4
print 'Average net util 5 : = ',avhop5
print 'Average net util 6 : = ',avhop6

