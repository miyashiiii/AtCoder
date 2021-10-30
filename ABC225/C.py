"""
https://atcoder.jp/contests/abc225/tasks/abc225_c

入力例
2 3
1 2 3
8 9 10

"""


def main():
    n, m = map(int, input().split())

    prev_list = list(map(int, input().split()))
    if prev_list[0] // 7 != prev_list[-1] // 7:
        if prev_list[-1] % 7 != 0:
            print("No")
            exit()

    for i, p in enumerate(prev_list):
        if i == 0:
            continue
        if p - prev_list[i - 1] != 1:
            print("No")
            exit()

    for i in range(n - 1):
        b_list = list(map(int, input().split()))
        for p, b in zip(prev_list, b_list):
            if b - p != 7:
                print("No")
                exit()
        prev_list = b_list
    print("Yes")


if __name__ == "__main__":
    main()
