class Solution:
    def digitCount(self, num: str) -> bool:
        c = Counter(num)
        i = 0

        for i in range(len(num)):
            if c[str(i)] != int(num[i]):
                return False
        
        return True
