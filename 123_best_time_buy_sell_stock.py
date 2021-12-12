"""
123. Best Time to Buy and Sell Stock III
Hard

4980

110

Add to List

Share
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).



Example 1:

Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
Example 4:

Input: prices = [1]
Output: 0

"""


def stock(a, buy=[], sell=[], i=0):
    if i>=len(a) or len(buy)==2 and len(sell)==2:
        return profit(a, buy, sell)
    max_profit = 0
    if len(buy)>len(sell):
        max_profit = max(max_profit, stock(a, buy, sell, i+1))
        sell.append(i)
        max_profit = max(max_profit, stock(a, buy, sell, i+1))
        sell.remove(i)
    elif len(buy)<2:
        max_profit = max(max_profit, stock(a, buy, sell, i+1))
        buy.append(i)
        max_profit = max(max_profit, stock(a, buy, sell, i+1))
        buy.remove(i)
    return max_profit

def profit(a, buy, sell):
    if len(buy)!=len(sell):
        return 0
    total = 0
    for i in range(len(buy)):
        total += a[sell[i]] - a[buy[i]]
    return total

print(stock([3,3,5,0,0,3,1,4]))
print(stock([1,2,3,4,5]))
print(stock([7,6,4,3,1]))
