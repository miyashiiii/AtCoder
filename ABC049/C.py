"""
https://atcoder.jp/contests/abc217/tasks/abc217_c

erasedream
"""

l = ["dream", "dreamer", "erase", "eraser"]
s = input()

while s != "":
    for phrase in l:
        if s.endswith(phrase):
            s = s[:-len(phrase)]
            break
        else:
            continue
    else:
        print("NO")
        exit()

print("YES")
