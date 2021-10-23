"""
https://atcoder.jp/contests/abc222/tasks/abc222_b

入力例
aaba


"""

s = input()

l = []
for i in range(len(s)):

    l.append(s[i:]+s[:i])

l.sort()
print(l[0])
print(l[-1])
