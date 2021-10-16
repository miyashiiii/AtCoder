"""
https://atcoder.jp/contests/abc221/tasks/abc221_b
入力例
abc
acb

"""
s = input()
t = input()

first_error_idx = 0
for i, c in enumerate(s):
    if c == t[i]:
        continue
    else:
        first_error_idx=i
        break
else:
    print("Yes")
    exit()

if s[first_error_idx] == t[first_error_idx + 1] and s[first_error_idx + 1] == t[first_error_idx]:
    print("Yes")
else:
    print("No")
