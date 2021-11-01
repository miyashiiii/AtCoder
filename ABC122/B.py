"""
https://atcoder.jp/contests/abc122/tasks/abc122_b

ATCODER
"""


def main():
    s = input()

    acgt = "ACGT"

    ans = 0
    length = 0

    for c in s:
        if c in acgt:
            length += 1
            ans = max(ans, length)
        else:
            length = 0

    print(ans)


if __name__ == "__main__":
    main()
