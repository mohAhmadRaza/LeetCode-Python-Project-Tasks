class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        res, n = [], len(code)

        if k > 0:
            for i in range(len(code)):
                if n - i > k:
                   res.append(sum(code[i+1:i+k+1]))
                else:
                    res.append(sum(code[i+1:]) + sum(code[0:k-(n-i+-1)]))
        
        elif k < 0:
            k = -k  # Use the absolute value of k for the negative case
            for i in range(n):
                if i >= k:
                    res.append(sum(code[i-k:i]))
                else:
                    res.append(sum(code[i-k:]) + sum(code[:i]))
        
        else:
            return [0]* (n)
        
        return res



