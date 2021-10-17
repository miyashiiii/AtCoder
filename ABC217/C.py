"""
https://atcoder.jp/contests/abc217/tasks/abc217_c
5
5 3 2 4 1
"""

_ = input()
p = input().split()

q = list(range(len(p)))

for i, pi in enumerate(p):
    q[int(pi) - 1] = i

ans = ""
for qi in q:
    if ans != "":
        ans += " "
    ans += str(qi + 1)

print(ans)

# print(str(np.argsort(p)+1)[1:-1])
