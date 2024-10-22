def min_coins(coins, target_amount):
    # structure to store the minimum number of coins for each outcome
    coin_tree = { i: target_amount for i in range(0, target_amount+1) }
    coin_tree[0] = 0 

    # For every amount till the target amount choose the minimum number of coins
    # that can make up the amount. Stop when the final target is reached
    for amount in range(1, target_amount+1):
        # Check every possible denomination and find the remainder subproblems
        for coin in coins:
            remainder = amount - coin
            # Include coin if the balance is not negative
            if remainder >= 0:
                coin_tree[amount] = min(coin_tree[amount], 1 + coin_tree[remainder])
            print("Current State:")
            print(coin_tree)

    return coin_tree[target_amount]
                
# coins = [1, 4, 6, 9, 14]
# target_amount = 26
# print(min_coins(coins, target_amount))

