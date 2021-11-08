"""
https://atcoder.jp/contests/abc226/tasks/abc226_c

入力例
3
3 0
5 1 1
7 1 1


"""
import sys

sys.setrecursionlimit(1000000)


def main():
    n = int(input())

    time = 0
    skill_times = []
    required_skills_list = []
    acquired_list = [False] * n

    def get_skills(skill_id):
        # skill_data = skills[skill_id]
        nonlocal time
        skill_time = skill_times[skill_id]
        time += skill_time
        # print(time)
        acquired_list[skill_id] = True

        # required_skills_num = skill_data[1]
        for required in required_skills_list[skill_id]:
            if not acquired_list[required - 1]:
                get_skills(required - 1)

    for i in range(n):
        skill = list(map(int, input().split()))
        skill_times.append(skill[0])
        required_skills_list.append(skill[2:])

    get_skills(n - 1)
    print(time)


if __name__ == "__main__":
    main()
