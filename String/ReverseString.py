class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        
        left, right, n = 0, k, len(s)

        while left < n:
            right = min(right, n)
            s = s[:left] + s[left:right][::-1] + s[right:]

            left += 2 * k
            right = left + k
        
        return s





            
            
