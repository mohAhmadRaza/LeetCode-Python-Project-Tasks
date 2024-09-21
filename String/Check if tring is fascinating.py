class Solution:
    def isFascinating(self, n: int) -> bool:
        n2, n3 = n * 2, n * 3

        string = str(n) + str(n2) + str(n3)
        string = list(string)
        return len(set(string)) == 9 and len(string) == 9 and '0' not in string
