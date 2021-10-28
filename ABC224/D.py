"""
https://atcoder.jp/contests/abc222/tasks/abc222_b

入力例
5
1 2
1 3
1 9
2 9
3 9
3 9 2 4 5 6 7 8

"""
from collections import deque


class State:
    def __init__(self, board, space, prev_state):
        self.board = board
        self.space = space
        self.prev_state = prev_state

    def __repr__(self):
        return str(self.board)


def bf_search(start, goal, edges):
    q = deque()
    q.append(State(start, start.index(0), None))
    table = {tuple(start): True}
    while len(q) > 0:
        a = q.popleft()
        for x in edges[a.space]:
            b = a.board[:]
            b[a.space] = b[x]
            b[x] = 0
            key = tuple(b)
            if key in table: continue
            c = State(b, x, a)
            if b == goal:
                print_answer(c)
                return
            q.append(c)
            table[key] = True


def print_answer(x):
    count = 0
    while True:
        print(x)
        x = x.prev_state
        if x is None:
            break
        count += 1
    print(count)
    exit()


def main():
    n = int(input())
    edges = [[] for _ in range(9)]
    for i in range(n):
        u, v = map(int, input().split())
        edges[u - 1].append(v - 1)
        edges[v - 1].append(u - 1)
    start = [int(v) for v in input().split()] + [0]
    goal = []
    for i in range(9):
        if i + 1 in start:
            goal.append(i + 1)
        else:
            goal.append(0)

    if start == goal:
        print(0)
        exit()
    bf_search(start, goal, edges)
    print(-1)


if __name__ == "__main__":
    main()
