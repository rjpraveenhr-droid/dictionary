D={4:15,14:50,9:19,14:5}
print(D)
print(D[4])#15
print(D.get(14))#5
print(D)

L=[9,1,7,0,5,12]
for x in L:
    print(x)

for k in D.keys():
    print("key : ",k)

for v in D.values():
    print("Values : ",v)

for k,v in D.items():
    print("key : ",k)
    print("Values : ",v)