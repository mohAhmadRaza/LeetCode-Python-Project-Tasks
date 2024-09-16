class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        L, count = set('aeiou'), 0
        
        left, right = 0, k
        for i in s[left : right]:
            if i in L:
                count += 1

        maxi = count

        for i in range(k, len(s)):
            if s[i] in L:
                count += 1
            if s[i-k] in L:
                count -= 1

            maxi = max(maxi, count)
        
        return maxi

            
