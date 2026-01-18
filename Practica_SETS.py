SET = set([1,2,(3,4),5])
#print(type(SET))
#print(SET)
#print(len(SET)) 

SET2 = {1,2,3,4,2,3,6,5,3,5,4}
#print(type(SET2))
#print(SET2)

s1={1,2,3}
s2={3,4,5}
s2.add(8)
s2.remove(8)
s3 = s1.union(s2)
sorteo = s3.pop()
s3.clear()
print(s3)