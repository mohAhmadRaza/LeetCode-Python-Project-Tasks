class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        c = Counter(chars)

        count = 0
        
        for i in words:
            if Counter(i) <= c:
                count += len(i)
            
        return count
