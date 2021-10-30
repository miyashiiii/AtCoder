"""
https://atcoder.jp/contests/abc225/tasks/abc225_b

入力例
5
1 4
2 4
3 4
4 5

"""


def main():
    n = int(input())
    a1, b1 = map(int, input().split())
    a2, b2 = map(int, input().split())
    root = None
    if a1 == a2 or a1 == b2:
        root = a1
    elif b1 == a2 or b1 == b2:
        root = b1
    else:
        print("No")
        exit()

    for _ in range(n - 3):
        a, b = map(int, input().split())
        if root not in [a, b]:
            print("No")
            exit()

    print("Yes")


if __name__ == "__main__":
    main()
