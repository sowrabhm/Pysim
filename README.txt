Author : Sowrabh Moily   (sowrabhm@winlab.rutgers.edu)

About Pysim:
   Python simulation to determine the path followed by a hop-by-hop routing protocol which is designed for scalable multicast. Assumptions are
that every router in the network exchanges periodic link state messages that are used to determine the shortest path to any node. Each function uses different approach to decide whether to split the packet or push it forward. Unlike source routing where the tree is once built 
and stored for future packets, hop by hop routing protocol has stateless routing with decision taken at every hop. This is useful when the 
destinations are mobile devices whose locations change regularly and are identified by a GUID instead of a network address.
[Refer http://mobilityfirst.winlab.rutgers.edu for complete information about the project ] 

   The networks that are used for testing the simulation are randomly generated networks having the jellyfish topology using a Matlab script from 
 https://bitbucket.org/romoore/gnrs/downloads. The weights of the links indicate the SETT's of the links

The aim of the simulation is to compare the performance of the developed hop-by-hop algorithms against the existing and most widely used 
PIM-SM {Protocol Independant Multicast-Sparse Mode}. Parameters for comparison include
1)The total number of hops / links traversed (Indicates utilization of network)
2)The average and median time delay from source to each individual destination
3)The maximum time taken to reach a destination in the multicast group. [Important for some applications with strict time constraint]
4)Runtime of the simulation. (Can be used to get an approximate idea of the )
