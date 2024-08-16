class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()

        if prices[0] + prices[1] <= money:
            return money - (prices[0] + prices[1])
        else:
            return money

Method 2:
class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        sortedPrices = sorted(prices)
        first = sortedPrices[0]
        second = sortedPrices[1]
        total = first + second

        if total <= money:
            return (money - total)
        return money
