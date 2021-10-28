"""
https://atcoder.jp/contests/abc201/tasks/abc201_c

ooo???xxxx

"""


def main():
    s = input()

    o_list = []
    x_list = []
    for i in range(len(s)):
        if s[i] == "o":
            o_list.append(str(i))
        elif s[i] == "x":
            x_list.append(str(i))

    ans = 0

    for i in range(10000):
        str_i = f"{i:04}"
        if str_i == "0123":
            print("")

        o_ok = True
        for o in o_list:
            if o not in str_i:
                o_ok = False
                break

        if not o_ok:
            continue

        x_ok = True
        for x in x_list:
            if x in str_i:
                x_ok = False
        if not x_ok:
            continue

        ans += 1
        # print(str_i)

    print(ans)


if __name__ == "__main__":
    main()
