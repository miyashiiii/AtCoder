"""
https://atcoder.jp/contests/abc199/tasks/abc199_c

2
FLIP
2
2 0 0
1 1 4
"""


def main():
    n = int(input())
    s = list(input())
    q = int(input())

    s1 = s[:n]
    s2 = s[n:]
    is_flip = False
    for i in range(q):
        t, a, b = map(int, input().split())
        if t == 2:
            is_flip = not is_flip
            continue

        if is_flip:
            s_first = s2
            s_second = s1
        else:
            s_first = s1
            s_second = s2

        if a <= n:
            idx_a = a - 1
            c_a = s_first[idx_a]
        else:
            idx_a = a - n - 1
            c_a = s_second[idx_a]

        if b <= n:
            idx_b = b - 1
            c_b = s_first[idx_b]
        else:
            idx_b = b - n - 1
            c_b = s_second[idx_b]

        if a <= n:
            s_first[idx_a] = c_b
        else:
            s_second[idx_a] = c_b

        if b <= n:
            s_first[idx_b] = c_a
        else:
            s_second[idx_b] = c_a

        # print(s1, s2)
    if is_flip:
        s = s2 + s1
    else:
        s = s1 + s2

    print("".join(s))


if __name__ == "__main__":
    main()
