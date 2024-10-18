class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)

        print(freq)
        values = sorted(freq.keys(), key=lambda x:freq[x])
        return values[:2]
