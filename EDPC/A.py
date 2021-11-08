"""
https://atcoder.jp/contests/dp/tasks/dp_a

4
10 30 40 20


"""


def main():
    int(input())
    heights = list(map(int, input().split()))

    min_costs = []
    for i in range(len(heights)):
        if i == 0:
            min_costs.append(0)
            continue

        if i == 1:
            min_costs.append(abs(heights[0] - heights[1]))
            continue

        cost1 = min_costs[i - 1] + abs(heights[i - 1] - heights[i])
        cost2 = min_costs[i - 2] + abs(heights[i - 2] - heights[i])

        min_costs.append(min(cost1, cost2))

    # print(min_costs)

    print(min_costs[-1])


if __name__ == "__main__":
    main()
