l = [
	[1,2],
	[3,4],
	[5,6]
]

for a,b in l:
    print('a',a,'b',b)

o = [1,2,3]
graph = {city:[] for city in o}
print('graph',graph)

l2 = [1,2,3]
s2 = set(l2)
l3 = [2,3,4]
s3 = set(l3)
s3 |= s2
print('s3',s3)