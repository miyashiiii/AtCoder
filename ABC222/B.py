"""
https://atcoder.jp/contests/abc222/tasks/abc222_b

入力例
4 50
80 60 40 0

"""

n, p = [int(v) for v in input().split()]
li = [int(v) for v in input().split()]

count = 0

for v in li:
    if v < p:
        count+=1

print(count)
