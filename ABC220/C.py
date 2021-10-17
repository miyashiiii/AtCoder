"""
https://atcoder.jp/contests/abc220/tasks/abc220_c
3
3 5 2
26
"""

n = int(input())
a = [int(c) for c in input().split()]
x = int(input())

reminder = x % sum(a)
sum_ = 0
count = x // sum(a) * len(a)
while sum_ <= reminder:
    sum_ += a[count % n]
    count += 1

print(count)
