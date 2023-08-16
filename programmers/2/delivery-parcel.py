from itertools import product


def solution(users, emoticons):
    arr = [10, 20, 30, 40]
    rates_arr = list(product(arr, repeat=len(emoticons)))
    results = []
    for rates in rates_arr:
        cnt, price = 0, 0

        for user in users:
            user_rate, user_price = user
            cur_cnt, cur_price = 0, 0

            for rate, emoticon_price in zip(rates, emoticons):

                if rate >= user_rate:
                    cur_price += (emoticon_price // 100 * (100 - rate))

                if cur_price >= user_price:
                    cur_cnt += 1
                    break

            if cur_cnt == 1:
                cnt += 1
            else:
                price += cur_price

        results.append([cnt, price])

    return sorted(results, key=lambda x: (-x[0], -x[1]))[0]


print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900],
      [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]))
