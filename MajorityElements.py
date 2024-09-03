class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        freq = Counter(nums)
        k = n // 3
        result = [a for a, b in freq.items() if b > k]

        return result
