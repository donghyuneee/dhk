DongHyun Kim
Touched by user2

def max(a,b,c):
  mx = None
  if a>b:
    if a>c:
      mx = a
    else:
      mx = c
  else:
    if b>c:
      mx=b
    else:
      mx=c
  return mx

x = int(input())
z = int(input())
z = int(input())

m = max(x,y,z)
print(m)
