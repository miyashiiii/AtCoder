"""
(AtCoder Beginners Selection)
https://atcoder.jp/contests/abs/tasks/abc085_c

9 45000
"""

n, y = [int(c) for c in input().split()]
count = 0
for i in range(n + 1):
    for j in range(n - i + 1):
        k = n - i - j
        if 10000 * i + 5000 * j + 1000 * k == y:
            print(f"{i} {j} {k}")
            exit()

print("-1 -1 -1")
