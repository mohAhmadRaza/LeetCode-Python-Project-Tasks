class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        freq = Counter(nums)
        count = 0

        vis = defaultdict(bool)
        
        for a, b in freq.items():
            complement = abs( a + k )
            if complement in freq.keys() and vis[complement] == False:
                count += freq[complement] * b
                vis[complement] = True
        
        return count
