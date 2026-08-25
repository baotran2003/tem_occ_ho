from typing import List
def maxProfit(prices: List[int]) -> int:

    # current_profit: int = 0
    # max_profit: int = 0
    #
    # for i in range(n):
    #     for j in range (i + 1, n):

    min_prices: int = prices[0]
    max_profit: int = 0

    n: int = len(prices)
    for i in range (1, n):
        if prices[i] < min_prices:
            min_prices = prices[i]
        else:
            current_profit: int = prices[i] - min_prices
            if current_profit > max_profit:
                max_profit = current_profit
    return max_profit

if __name__ == "__main__":
    prices = [2, 1, 5, 0, 4, 6]
    print("Lợi nhuận lớn nhất :", maxProfit(prices))

    # max (sell - buy)