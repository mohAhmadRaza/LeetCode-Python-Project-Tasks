class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = []
        for ind, i in enumerate(words):
            freq = Counter(i)
            if x in i:
                res.append(ind) 
            else:
                continue
        
        return res
