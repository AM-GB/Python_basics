# put your python code here
n = []
while True:
  st = [i for i in input().split()]
  if st == ['end']:
    break
  for j in range(len(st)):
    st[j] = int(st[j])
  n.append(st)



print(n)
print(len(n[1]))
print(len(n))