"""
https://atcoder.jp/contests/abc222/tasks/abc222_c入力例
2 3
GCP
PPP
CCC
PPC

"""

n, m = [int(v) for v in input().split()]

a_list = []

for match_idx in range(2 * n):
    a_list.append(input())


def is_win_1st(hand1, hand2):
    if hand1==hand2:
        return None
    return (hand1 == "G" and hand2 == "C") or (hand1 == "C" and hand2 == "P") or (hand1 == "P" and hand2 == "G")


def order_from_scores(scores):
    score_dict = {}
    for i, s in enumerate(scores):
        if s in score_dict:
            score_dict[s].append(i)
        else:
            score_dict[s] = [i]
    sorted_tuple = sorted(score_dict.items(), reverse=True)
    ret = []
    for k, v in sorted_tuple:
        ret += v
    return ret


scores = [0] * 2 * n
order = order_from_scores(scores)

for match_idx in range(m):
    # for player_order, player_id in range(order):
    for i in range(n):

        player_order1 = i * 2
        player_order2 = i * 2 + 1

        player_id1 = order[player_order1]
        player_id2 = order[player_order2]

        hand1 = a_list[player_id1][match_idx]
        hand2 = a_list[player_id2][match_idx]

        # print(player_id1, "-", player_id2)
        is_win = is_win_1st(hand1, hand2)
        if is_win is None:
            continue
        if is_win:
            scores[player_id1] += 1
        else:
            scores[player_id2] += 1

    # print(scores)
    order = order_from_scores(scores)
    # print(order)

for n in order:
    print(n + 1)
