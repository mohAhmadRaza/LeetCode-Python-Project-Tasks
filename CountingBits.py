Method 1:

class Solution:
    def countBits(self, n):
        ans = [0] * (n + 1)  # Initialize an array of size n+1 with all values set to 0
        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)  # Calculate the number of 1's for each i
        return ans


Method 2:
class Solution:
    def countBits(self, n: int) -> List[int]:
        L = []
        for i in range(0, n+1):
            s = bin(i)
            L.append(s.count("1"))
        
        return L
