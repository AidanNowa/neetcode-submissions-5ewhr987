class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        best_total = 0
        curr_max = prices[0]
        curr_min = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < curr_min:
                curr_min = prices[i]
                curr_max = prices[i]
            elif prices[i] > curr_max:
                curr_max = prices[i]
                total = curr_max - curr_min
                if total > best_total:
                    best_total = total
        return best_total
            
            