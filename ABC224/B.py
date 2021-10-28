"""
https://atcoder.jp/contests/abc224/tasks/abc224_b

入力例
3 3
2 1 4
3 1 3
6 4 1

"""


def main():
    h, w = map(int, input().split())
    matrix = []
    for i in range(h):
        row = map(int, input().split())
        matrix.append(list(row))
    # print(matrix)

    for i1 in range(h):
        for i2 in range(h):
            if i1 >= i2:
                continue
            for j1 in range(w):
                for j2 in range(w):
                    if j1 >= j2:
                        continue
                    if matrix[i1][j1] + matrix[i2][j2] > matrix[i2][j1] + matrix[i1][j2]:
                        print("No")
                        exit()
    print("Yes")


if __name__ == "__main__":
    main()
