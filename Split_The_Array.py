class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        if len(nums) % 2 == 1:
            return False
        
        fre = Counter(nums)

        count = [1 for key, value in fre.items() if value == 1]
        print(count)
        for key, value in fre.items():
            if value > 1 and value % 2 == 1 or value > 2:
                return False

        
        return sum(count) % 2 == 0
