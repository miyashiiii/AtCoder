"""
(AtCoder Beginners Selection)
https://atcoder.jp/contests/abs/tasks/abc087_b

2
2
2
100
"""

import itertools

l_a = [v for v in range(int(input()) + 1)]
l_b = [v for v in range(int(input()) + 1)]
l_c = [v for v in range(int(input()) + 1)]
x = int(input())

count = 0

p = itertools.product(l_a, l_b, l_c)

for a, b, c in p:
    sum_ = sum([a * 500, b * 100, c * 50, ])
    # print(sum_)
    if sum_ == x:
        count += 1

print(count)
