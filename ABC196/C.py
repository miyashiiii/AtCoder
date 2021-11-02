"""
https://atcoder.jp/contests/abc196/tasks/abc196_c

33


"""


def main():
    n = int(input())

    m = 1
    ans = 0
    while int(f"{m}{m}") <= n:
        ans += 1
        m += 1
    print(ans)


if __name__ == "__main__":
    main()
