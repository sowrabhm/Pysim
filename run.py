import mainfunc

res1=mainfunc.main(10)
print "Finished 4 destinations"
res2=mainfunc.main(20)
print "Finished 8 destinations"
res3=mainfunc.main(30)
print "Finished 16 destinations"
res4=mainfunc.main(40)
print "Finished 32 destinations"
res5=mainfunc.main(50)
print "Finished 64 destinations"
res6=mainfunc.main(60)
print "Finished 64 destinations"
res7=mainfunc.main(70)
print "Finished 64 destinations"
res8=mainfunc.main(80)
print "Finished 64 destinations"


algo1hop=[res1[0],res2[0],res3[0],res4[0],res5[0],res6[0],res7[0],res8[0]]
algo2hop=[res1[1],res2[1],res3[1],res4[1],res5[1],res6[1],res7[1],res8[1]]
algo4hop=[res1[2],res2[2],res3[2],res4[2],res5[2],res6[2],res7[2],res8[2]]
algo5hop=[res1[3],res2[3],res3[3],res4[3],res5[3],res6[3],res7[3],res8[3]]
algo6hop=[res1[4],res2[4],res3[4],res4[4],res5[4],res6[4],res7[4],res8[4]]


print "Algo 1:", algo1hop
print "Algo 2:", algo2hop
print "Algo 5:", algo5hop
print "Algo 6:", algo6hop
