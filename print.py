s=int(input())
p=[int(i) for i in input().split()]
p1=[]
for i in range(0,len(p)):
  if i==p[i]:
    p1.append(p[i])
if len(p1)==0:
  print("-1")
else:
  for k in range(len(l1)):
     print(p1[k],end=" ")
