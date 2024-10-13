class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = Counter(nums)
        sortFreq = list(sorted(freq.values(), reverse=True))

        return sortFreq[0] * sortFreq.count(sortFreq[0])
