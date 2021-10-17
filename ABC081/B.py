"""
(AtCoder Beginners Selection)
https://atcoder.jp/contests/abs/tasks/abc081_b

3
8 12 40
"""

_ = input()
p = input().split()

min_count = 10 ** 9

for c in p:
    n = int(c)
    count = 0
    while n % 2 == 0:
        n /= 2
        count += 1
    if min_count > count:
        min_count = count

print(min_count)
