
# 把每一行的数字分隔后转化成int列表
a = [30 ,1]
b = sorted(a, reverse=True)
res = ''
for item in b:
    res += str(item)
print(res)
