class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        pairs = Counter(nums)

        p, r = 0, 0

        for key, value in pairs.items():
            p += value // 2
            r += value % 2
        
        return [p, r]
