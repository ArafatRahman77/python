list=[1,2,3,4]
for x in list:
    print(x)

print("let use range")

for x in range(len(list)):
    print(list[x])

rlist=[] 

for x in range(len(list)):
    z=list.pop()
    rlist.append(z)

print("Reversed:",rlist)    

