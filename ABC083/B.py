"""
(AtCoder Beginners Selection)
https://atcoder.jp/contests/abs/tasks/abc083_b

20 2 5
"""

n, a, b = [int(c) for c in input().split()]
sum_ = 0
for i in range(1, n + 1):
    # print(i)
    tmp_sum = 0
    for c in str(i):
        tmp_sum += int(c)
    if a <= tmp_sum <= b:
        sum_ += i

print(sum_)
