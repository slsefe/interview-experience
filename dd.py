# coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。
import sys

if __name__ == "__main__":
    # 读取第一行的n
    n = 5
    avid = [2, 3, 4, 5, 6]
    d = dict()
    d[2] = 1
    d[3] = 1
    d[4] = 3
    d[5] = 4
    d[6] = 4
    d2 = dict()
    for i in range(len(avid)):
        temp = avid[i]
        while temp in d:
            temp = d[temp]
        if temp not in d2:
            d2[temp] = 1
        else:
            d2[temp] += 1
    av_id = 0
    n_avid = 0
    for k, v in d2.items():
        if v > n_avid:
            av_id = k
            n_avid = v
        elif v == n_avid and k > av_id:
            av_id = k
            n_avid = v
    print(av_id)
