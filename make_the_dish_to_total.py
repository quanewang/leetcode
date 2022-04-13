# Input: a list of items, each comes with a name and price, e.g., {"soup": 4.5, "fries": 2, "fish": 9}. For a given target amount, say 11, find out all possible combinations that sum up to this amount. Note that each item can be chosen multiple times in one combination. In this case, it would be two possible combinations as follows:
# [
# {soup * 2), fries * 1}.
# {fish * 1, fries * 1},
# ]

EPS = 1e-6
items = {"soup": 4.5, "fries": 2, "fish": 9}

def dish(items, total):
    return dish_helper(items, total)


# picked: [(soup, 2), (dish, 2)]
def dish_help(items, total, i=0, picked=[]):
    if not items:
        return []
    precheck = check(items, total, picked)
    if precheck < 0:
        return []
    elif not precheck:
        return [picked]
    elif i == len(items):
        return []

    result = []

    keys = items.keys()
    max_count = total // items[keys[i]]
    for j in range(max_count + 1):
        import copy
        picked_copy = copy.copy(picked)
        if j > 0:
            picked.append((keys[i], j))
        result_j = dish_help(items, total, i + 1, picked)
        result.extend(result_j)
    return result


def check(items, total, picked):
    for p in picked:
        total -= items[p[0]] * p[1]
    if total < EPS * (-1):
        return -1
    elif abs(total) < EPS:
        return 0


print([0] * 5)
print([[0]*5]*5)
