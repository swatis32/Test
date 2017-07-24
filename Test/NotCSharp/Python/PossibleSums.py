# https://codefights.com/interview-practice/task/rMe9ypPJkXgk3MHhZ
import itertools
from collections import defaultdict

def possibleSums2(coins, quantity):
    sum_set = set()
    coins_dict = defaultdict(int)
    list_coins = []
    i = 0
    for c in coins:
        qty = quantity[i]
        coins_dict[c] = coins_dict[c] + qty
        i = i + 1

    for k, v in coins_dict.items():
        x = [k for i in range(0, v)]
        list_coins = list_coins + x

    for L in range(1, len(list_coins) + 1):
        for subset in itertools.combinations(list_coins, L):
            sum_set.add(sum(subset))

    print(len(sum_set))
    return len(sum_set)


# possibleSums([3, 1, 1], [111, 84, 104])
# possibleSums([1, 2, 3], [2, 3, 10000])
# possibleSums([10, 50, 100], [1, 2, 1])