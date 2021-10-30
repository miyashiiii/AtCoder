"""
https://atcoder.jp/contests/abc225/tasks/abc225_d

入力例
7 14
1 6 3
1 4 1
1 5 2
1 2 7
1 3 5
3 2
3 4
3 6
2 3 5
2 4 1
1 1 5
3 2
3 4
3 6


"""


class Car:

    def __init__(self, prev=-1, next=-1):
        self.prev = prev
        self.next = next


def main():
    n, m = map(int, input().split())
    cars = [Car() for _ in range(n)]
    # starts = []

    for i in range(m):
        q = list(map(int, input().split()))
        if q[0] == 1:
            _, x, y = q
            x -= 1
            y -= 1
            cars[x].next = y
            cars[y].prev = x
        elif q[0] == 2:
            _, x, y = q
            x -= 1
            y -= 1
            cars[x].next = -1
            cars[y].prev = -1
        else:
            _, x = q
            x -= 1

            after = []
            tmp = x
            while True:
                next = cars[tmp].next
                if next == -1:
                    break
                after.append(str(next + 1))
                tmp = next

            before = []
            tmp = x
            while True:
                prev = cars[tmp].prev
                if prev == -1:
                    break
                before.insert(0, str(prev + 1))
                tmp = prev

            ans = before + [str(x + 1)] + after
            print(f"{len(ans)} {' '.join(ans)}")


if __name__ == "__main__":
    main()
