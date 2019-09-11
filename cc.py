import sys

m, n = '00002', '0A130'
d = dict()
keys = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
        'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
for i in range(36):
    d[keys[i]] = i
max = 0
for j in m:
    if d[j] >= max:
        max = d[j]
for k in n:
    if d[k] >= max:
        max = d[k]
max += 1
for p in range(max, 36):
    hour = 0
    for i in range(len(m)):
        hour += d[m[i]] * (p ** (len(m)-1-i))
    if hour < 0 or hour > 23:
        break
    minute = 0
    for j in range(len(n)):
        minute += d[n[j]] * (p ** (len(n)-1-j))
    if minute < 0 or minute > 59:
        break
    print(p)
