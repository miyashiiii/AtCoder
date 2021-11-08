"""
https://atcoder.jp/contests/dp/tasks/dp_b

4
10 30 40 20


"""


def main():
    _, k = map(int, input().split())
    heights = list(map(int, input().split()))

    min_costs = []
    for i in range(len(heights)):
        if i == 0:
            min_costs.append(0)
            continue

        min_cost = 10 ** 100
        for j in range(1, k + 1):
            if j > i:
                break
            min_cost = min(min_cost, min_costs[i - j] + abs(heights[i - j] - heights[i]))

        # print(costs)
        min_costs.append(min_cost)

    # print(min_costs)

    print(min_costs[-1])


if __name__ == "__main__":
    main()
