import random
import os
import sys

max=int(sys.argv[1])
node_no=int(sys.argv[2])
print "Max is ",max ,"and nods are ",node_no
dest=[x for x in range(1,max+1)]
r= random.sample(dest,node_no)
f=open("destinations.txt",'w')
for node in r:
   f.write(str(node) +"\n")
f.close() 

