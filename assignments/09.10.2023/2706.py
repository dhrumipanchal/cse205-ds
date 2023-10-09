class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        ans=sum(prices[:2])
        result=money-ans
        return result if result>=0 else money