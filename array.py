mn=int(input())
r1=list(map(int,input().split()))
s=0
for i in range(mn):
  for j in range(i,mn):
    for t in range(j,mn):
      if(r1[i]<r1[j]<r1[t]):
        s+=1
print(s)
