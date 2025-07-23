class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        counted = Counter(nums)
        result = []
        heapq.heapify(result)

        for key, value in counted.items():
            heapq.heappush(result, (-value, key))
        
        for i in range(k):
            nums[i] = heapq.heappop(result)[1]
        
        return nums[0:k]
    
