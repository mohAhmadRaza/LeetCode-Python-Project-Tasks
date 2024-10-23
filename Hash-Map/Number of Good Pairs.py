class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        freq = Counter(nums)
        pairs = 0

        for a, b in freq.items():
            if b > 1:
                pairs += (b*(b-1))//2
        
        return pairs
