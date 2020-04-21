
# Classic knapsack problem, dynamic approach. Each array field contains max value that can be achieved
# with given amount of items and given amount of remaining weight.
# A mock 0th item was added to the item arrays, so that the indices match with what is going on in the
# array used for the dynamic algorithm


def knapsack(item, rem_weight):
    # already calculated
    if sub_results[item][rem_weight] is not None:
        return sub_results[item][rem_weight]
    # can't add item
    elif weights[item] > rem_weight:
        sub_results[item][rem_weight] = knapsack(item - 1, rem_weight)
        return sub_results[item][rem_weight]
    # can add item - enslaved recursion
    else:
        sub_results[item][rem_weight] = max(
            knapsack(item - 1, rem_weight),
            knapsack((item - 1), rem_weight - weights[item]) + values[item]
        )
        return sub_results[item][rem_weight]


if __name__ == "__main__":
    max_weight = 5
    weights = [-1, 5, 3, 4, 2]
    values = [-1, 60, 50, 70, 30]
    sub_results = [[None for i in range(max_weight + 1)] for j in range(len(values))]
    for i in range(max_weight + 1):
        sub_results[0][i] = 0

    item_count = len(weights) - 1
    print(knapsack(item_count, max_weight))
