
def quick_sort(l1):
    if len(l1)<=1:
        return l1
    pivot = l1[0]
    left = []
    right = []
    for val in l1[1:]:
        if val < pivot:
            left.append(val)
        else:
            right.append(val)
    return quick_sort(left) + [pivot] + quick_sort(right)
if __name__ == "__main__":
    # 读取每一行
    a = [30,1]
    b = quick_sort(a)
    res = ''
    for item in b[::-1]:
        res+=str(item)
    print(str(res))