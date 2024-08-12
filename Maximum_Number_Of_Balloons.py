from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon = Counter(text)

        # Count each required character; default to 0 if not present
        b_count = balloon.get('b', 0)
        a_count = balloon.get('a', 0)
        l_count = balloon.get('l', 0) // 2  # Need pairs of 'l'
        o_count = balloon.get('o', 0) // 2  # Need pairs of 'o'
        n_count = balloon.get('n', 0)
        
        # Find the minimum count among the required characters
        minimum = min(b_count, a_count, l_count, o_count, n_count)

        return minimum
