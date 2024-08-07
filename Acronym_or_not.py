class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        acronym = ""

        for i in words:
            acronym += i[0]
        
        return acronym == s
