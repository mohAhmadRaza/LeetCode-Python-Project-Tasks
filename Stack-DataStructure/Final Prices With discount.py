class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        
        stack = []
        res = [0] * len(prices) 
        

        for i in range(len(prices)):
            
            while stack and prices[stack[-1]] >= prices[i]:
                res[stack[-1]] = prices[stack[-1]] - prices[i]
                stack.pop()
            
            stack.append(i)
        
        for i in stack:
            res[i] = prices[i]
            
        return res

            
        
