"""
https://atcoder.jp/contests/abc223/tasks/abc223_c

入力例
3
1 3
2 2
3 1


"""
n =int(input())

length_list = []
speed_list = []
times = []

for i in range(n):
    a,b = map(int,input().split())
    length_list.append(a)
    speed_list.append(b)
    times.append(a/b)

total_time = sum(times)
# print(times)
# print(total_time)

remain_time = total_time/2
ans_idx = 0
for i,time in enumerate(times):
    if time<remain_time:
        remain_time-=time
    elif time==remain_time:
        print(sum(length_list[:i+1]))
        exit()
    else:
        ans_idx = i
        break

ans_length = sum(length_list[:ans_idx])
ans_length+=remain_time*speed_list[ans_idx]
print(ans_length)
# print(remain_time)

