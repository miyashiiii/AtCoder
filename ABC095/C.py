"""
https://atcoder.jp/contests/abc095/tasks/arc096_a

1500 2000 1600 3 2

"""


def main():
    a, b, c, x, y = [int(v) for v in input().split()]

    # A,Bピザをそれぞれ買う場合
    ans1 = a * x + b * y

    # ABピザを最少で買う場合
    if x >= y:
        ans2 = (y * 2) * c + (x - y) * a
    else:
        ans2 = (x * 2) * c + (y - x) * b

    # すべてABピザで買う場合
    if x >= y:
        ans3 = x * 2 * c
    else:
        ans3 = y * 2 * c

    print(min(ans1, ans2, ans3))


if __name__ == "__main__":
    main()
