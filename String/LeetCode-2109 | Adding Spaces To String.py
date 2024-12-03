class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        array = []
        start = 0

        for i in range(len(spaces)):
            array.append(s[start:spaces[i]])

            start = spaces[i]
        
        array.append(s[spaces[-1]:])
        
        return ' '.join(array)
