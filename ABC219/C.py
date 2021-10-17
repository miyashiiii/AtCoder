"""
https://atcoder.jp/contests/abc219/tasks/abc219_c
bacdefghijklmnopqrstuvwxzy
4
abx
bzz
bzy
caa


"""

x = input()
n = int(input())

members = []  # [[score, name]]
for _ in range(n):
    name = input()
    score = 0
    for i, c in enumerate(name):
        score += x.index(c) * 26 ** (10 - i - 1)
    members.append([score, name])

members.sort()

for m in members:
    print(m[1])
