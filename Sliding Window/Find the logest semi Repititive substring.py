class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        if len(set(list(s))) == 1:
            return 2 if len(s) > 2 else len(s)

        value = float('-inf')
        left, right, found, duplicate = 0, 1, False, 0

        while left < len(s) and right < len(s):
            if s[right] != s[right - 1]:
                right += 1
            
            elif s[right] == s[right -1] and not found:
                found = True
                duplicate = right
                right += 1
            
            elif s[right] == s[right - 1] and found:
                value = max(value, right - left )
                left = duplicate
                duplicate = 0
                found = False

        value = max(value, right - left)
        return value
