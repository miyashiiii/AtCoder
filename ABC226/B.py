"""
https://atcoder.jp/contests/abc226/tasks/abc226_b

入力例
4
2 1 2
2 1 1
2 2 1
2 1 2

"""


def main():
    n = int(input())
    arrays = set()
    for i in range(n):
        arr = tuple((map(int, input().split())))[1:]
        arrays.add(arr)

    print(len(arrays))


if __name__ == "__main__":
    main()
