class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = Counter(nums)

        sortedFrequencies = sorted(frequencies.items(), key=lambda x:x[1], reverse=True)
        againDict = collections.OrderedDict(sortedFrequencies)
        return list(againDict.keys())[:k]
