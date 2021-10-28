"""
https://atcoder.jp/contests/abc198/tasks/abc198_c

5 15 0

"""
import math


def main():
    r, x, y = map(int, input().split())
    distance = math.sqrt(x ** 2 + y ** 2)
    # print(math.ceil(distance / r))

    if distance < r:
        print(2)

    else:
        print(math.ceil(distance / r))


if __name__ == "__main__":
    main()
