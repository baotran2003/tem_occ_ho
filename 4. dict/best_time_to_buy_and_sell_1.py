from typing import List
def maxProfit(prices: List[int]) -> int:
    # max_profit: int = 0
    n: int = len(prices)
    #
    # for i in range (n):
    #     for j in range (i + 1, n):
    #         current_profit: int = prices[j] - prices[i]
    #
    #         if current_profit > max_profit:
    #             max_profit = current_profit
    # return max_profit

    min_price: int = prices[0]
    max_profit: int = 0

    for i in range (1, n):
        #1. neu gia hom nay be hon min_price, update lai gia mua
        if prices[i] < min_price:
            min_price = prices[i]

        #2. Neu gia ban ko thap hon, tinh thu loi nhuan hom nay
        else:
            current_profit:int = prices[i] - min_price
            #2.1 Update lai max_profit neu loi nhuan cao hon
            if current_profit > max_profit:
                max_profit = current_profit

    return max_profit

if __name__ == "__main__":
    prices = [2, 1, 5, 0, 4, 6]
    print("Lợi nhuận lớn nhất :", maxProfit(prices))



