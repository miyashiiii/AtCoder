"""
(AtCoder Beginners Selection)
https://atcoder.jp/contests/abs/tasks/arc089_a

2
3 1 2
6 1 1
"""


def count_divisor(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count


def main():
    n = int(input())
    if n == 105:
        print(1)
        return
    if n < 105:
        print(0)
        return

    count = 0
    for i in range(105, n + 1, 2):
        # print(i)
        divisors = count_divisor(i)
        # print("divisors:", divisors)
        if divisors == 8:
            count += 1

    print(count)


if __name__ == "__main__":
    main()
