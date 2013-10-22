import functionpim
import functiongpim
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
max1=[]
max2=[]
max4=[]
max5=[]
max6=[]
mean1=[]
mean2=[]
mean4=[]
mean5=[]
mean6=[]
median1=[]
median2=[]
median4=[]
median5=[]
median6=[]

subprocess.call(['./hello.sh'])

for i in range(0,20):
 
  
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
  max1.append(res1[3])
  mean1.append(res1[4])
  median1.append(res1[5])

  res2=function2.function2(G,source,dstlist2)
  cost2.append(res2[0])
  runtime2.append(res2[1])
  hop2.append(res2[2])
  max2.append(res2[3])
  mean2.append(res2[4])
  median2.append(res2[5])

  res4=function4.function4(G,source,dstlist3,5)
  cost4.append(res4[0])
  runtime4.append(res4[1])
  hop4.append(res4[2])
  max4.append(res4[3])
  mean4.append(res4[4])
  median4.append(res4[5])

  res5=function5.function5(G,source,dstlist4,5)
  cost5.append(res5[0])
  runtime5.append(res5[1])
  hop5.append(res5[2])
  max5.append(res5[3])
  mean5.append(res5[4])
  median5.append(res5[5])

  res6=functionpim.functionpim(G,source,dstlist3)
  cost6.append(res6[0])
  runtime6.append(res6[1])
  hop6.append(res6[2])
  max6.append(res6[3])
  mean6.append(res6[4])
  median6.append(res6[5])

#for i in range(0,len(cost1)):
 #print " ",cost1[i],"|",cost2[i],"|",cost4[i],"|",cost5[i],"|",cost6[i],"|",runtime1[i],"|",runtime2[i],"|",runtime4[i],"|",runtime5[i],"|",runtime6[i]
 #print " ", hop1[i], " | ", hop2[i], " | ", hop4[i], " | ", hop5[i], " | ", hop6[i], " | "
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

summax1=0
summax2=0
summax4=0
summax5=0
summax6=0

summean1=0
summean2=0
summean4=0
summean5=0
summean6=0

summedian1=0
summedian2=0
summedian4=0
summedian5=0
summedian6=0

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

 summax1=summax1+max1[i]
 summax2=summax2+max2[i]
 summax4=summax4+max4[i]
 summax5=summax5+max5[i]
 summax6=summax6+max6[i]
 
 summean1=summean1+mean1[i]
 summean2=summean2+mean2[i]
 summean4=summean4+mean4[i]
 summean5=summean5+mean5[i]
 summean6=summean6+mean6[i]
 
 summedian1=summedian1+median1[i]
 summedian2=summedian2+median2[i]
 summedian4=summedian4+median4[i]
 summedian5=summedian5+median5[i]
 summedian6=summedian6+median6[i]


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

avmax1=float(summax1)/len(max1)
avmax2=float(summax2)/len(max1)
avmax4=float(summax4)/len(max1)
avmax5=float(summax5)/len(max1)
avmax6=float(summax6)/len(max1)

avmean1=float(summean1)/len(mean1)
avmean2=float(summean2)/len(mean1)
avmean4=float(summean4)/len(mean1)
avmean5=float(summean5)/len(mean1)
avmean6=float(summean6)/len(mean1)

avmedian1=float (summedian1)/len(median1)
avmedian2=float (summedian2)/len(median1)
avmedian4=float (summedian4)/len(median1)
avmedian5=float (summedian5)/len(median1)
avmedian6=float (summedian6)/len(median1)



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

print 'Average max time 1: = ',avmax1
print 'Average max time 2: = ',avmax2
print 'Average max time 4: = ',avmax4
print 'Average max time 5: = ',avmax5
print 'Average max time 6: = ',avmax6

print 'Average mean time 1: = ',avmean1
print 'Average mean time 2: = ',avmean2
print 'Average mean time 4: = ',avmean4
print 'Average mean time 5: = ',avmean5
print 'Average mean time 6: = ',avmean6

print 'Average median time 1: =', avmedian1
print 'Average median time 2: =', avmedian2
print 'Average median time 4: =', avmedian4
print 'Average median time 5: =', avmedian5
print 'Average median time 6: =', avmedian6


