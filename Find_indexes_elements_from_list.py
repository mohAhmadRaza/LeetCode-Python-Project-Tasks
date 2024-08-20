class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        indexes = [ind for ind, value in enumerate(words) if x in value]
        return indexes
