class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        # Declaring Left Pointer
        Left = 0

        # Variable to store count of good strings
        GoodStrings = 0

        for right in range(3, len(s)+1):
            if len(set(s[Left:right])) == 3:
                GoodStrings += 1
            Left += 1
        
        return GoodStrings

