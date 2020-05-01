# put your python code here
n = []
while True:
  st = [i for i in input().split()]
  if st == ['end']:
    break
  for j in range(len(st)):
    st[j] = int(st[j])
  n.append(st)

result = [[0 for j in range(len(n[0]))] for i in range(len(n))]

for i in range(len(n)):
  for j in range(len(n[i])):
    for di in range(-1, 2):
      for dj in range(-1, 2):
        ai = i + di
        if (di != 0 and dj == 0) or (di == 0 and dj != 0):
          aj = j + dj
          if 0 <= ai < len(n) and 0 <= aj < len(n[i]):
            result[i][j] = result[i][j] + n[ai][aj]
          elif ai < 0:
            result[i][j] = result[i][j] + n[len(n) - 1][aj]
          elif ai == len(n):
            result[i][j] = result[i][j] + n[0][aj]
          elif aj < 0:
            result[i][j] = result[i][j] + n[ai][len(n[i]) - 1]
          elif aj == len(n[i]):
            result[i][j] = result[i][j] + n[ai][0]
st = ''
for i in range(len(result)):
  for j in range(len(result[i])):
    st = st + f'{result[i][j]} '
  print(st)
  st = ''