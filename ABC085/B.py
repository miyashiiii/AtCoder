"""
(AtCoder Beginners Selection)
https://atcoder.jp/contests/abs/tasks/abc085_b

4
10
8
8
6
"""

n = int(input())
l = []
for _ in range(n):
    n = int(input())
    l.append(n)

print(len(set(l)))

