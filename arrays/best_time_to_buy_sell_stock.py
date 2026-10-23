# Problem: Best Time to Buy and Sell Stock
# Difficulty: Easy
# Pattern:
# Time:   |  Space:
#
# Given a list `prices` where prices[i] is the price of a stock on day i,
# return the maximum profit from buying on one day and selling on a later
# day. If no profitable trade is possible, return 0. (You must buy before
# you sell.)
#
# Examples:
#   max_profit([7, 1, 5, 3, 6, 4])  -> 5   # buy at 1, sell at 6
#   max_profit([7, 6, 4, 3, 1])     -> 0   # prices only fall, no trade
#   max_profit([2, 4, 1])           -> 2   # buy at 2, sell at 4
#   max_profit([1])                 -> 0

def max_profit(prices):
    best_profit = 0
    buy_day = 0
    sell_day = 0
    while sell_day < len(prices):
        if prices[sell_day] > prices[buy_day]:
            profit = prices[sell_day] - prices[buy_day]
            if profit > best_profit:
                best_profit = profit
        elif prices[sell_day] < prices[buy_day]:
            buy_day = sell_day
        sell_day += 1
    return best_profit

# Single variable version
# def max_profit(prices):
#     best = 0
#     min_price = float("inf")   # cheapest price seen so far
#     for price in prices:
#         if price < min_price:
#             min_price = price          # found a cheaper buy day
#         else:
#             best = max(best, price - min_price)   # try selling today
#     return best


if __name__ == "__main__":
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5
    assert max_profit([7, 6, 4, 3, 1]) == 0
    assert max_profit([2, 4, 1]) == 2
    assert max_profit([1]) == 0
    print("passed")