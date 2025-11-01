class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                # Found a mismatch - try skipping one character
                # Option 1: Skip left character
                temp1, temp2 = left + 1, right
                while temp1 < temp2 and s[temp1] == s[temp2]:
                    temp1 += 1
                    temp2 -= 1
                
                if temp1 >= temp2:  # Successfully formed palindrome
                    return True
                
                # Option 2: Skip right character
                temp1, temp2 = left, right - 1
                while temp1 < temp2 and s[temp1] == s[temp2]:
                    temp1 += 1
                    temp2 -= 1
                
                if temp1 >= temp2:  # Successfully formed palindrome
                    return True
                
                return False  # Neither option worked
        
        return True
