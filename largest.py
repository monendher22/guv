u == int(input())
st = sorted(list(input().split()),reverse = True)
output = ' '.join(st)
if int(output) != 0:
  print(output)
else:
  print(0)
