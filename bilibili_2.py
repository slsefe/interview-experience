n = 5
s = 7
p = [1, 2, 3, 4, 5]
sum_p = 0
flag = 0
for i in p:
    sum_p += i
if sum_p <= s:
    print(-1)
else:
    for j in range(n):
        if flag == 0:
            for m in range(0, n-j):
                res = 0
                for k in range(m, j + 1 + m):
                    res += p[k]
                if res >= s:
                    print(j+1)
                    flag = 1
                    break
