"""
https://atcoder.jp/contests/abc222/tasks/abc222_b

入力例
5 2
3 4
2 4

"""
import itertools

n, m = map(int, input().split())
conds = []

for i in range(m):
    a, b = map(int, input().split())
    conds.append([a, b])

cond_unique = set(itertools.chain.from_iterable(conds))

not_used_on_cond = list(set(range(1, n + 1)) - cond_unique)

print(not_used_on_cond)
p = itertools.permutations(cond_unique)
valids = []
l = []
for seq in p:
    for a, b in conds:
        if seq.index(a) > seq.index(b):
            break
    else:
        valids.append(seq)

if len(valids) != 0:
    not_used_on_cond += [valids[0][0]]
    not_used_on_cond.sort()
    idx = not_used_on_cond.index(valids[0][0])
    left = not_used_on_cond[:idx]
    right = not_used_on_cond[idx + 1:]
    print(" ".join(map(str, left + list(valids[0]) + right)))
else:
    print(-1)
