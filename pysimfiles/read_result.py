import pickle

runtime1=pickle.load( open( "result.p", "rb" ) )
print "Cost1=",runtime1 
print "I=",len(runtime1)
cost1=pickle.load( open( "result.p", "rb" ) )
print "Cost1=",cost1
print "I=",len(cost1)

