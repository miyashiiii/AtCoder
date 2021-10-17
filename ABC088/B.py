"""
(AtCoder Beginners Selection)
https://atcoder.jp/contests/abs/tasks/abc088_b

4
20 18 2 18
"""

_ = input()
l = [int(c) for c in input().split()]

l.sort(reverse=True)

a = l[0::2]
b = l[1::2]

print(sum(a) - sum(b))
