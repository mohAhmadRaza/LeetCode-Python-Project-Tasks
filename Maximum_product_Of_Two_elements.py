class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        heap = []

        for i in nums:
            heapq.heappush(heap, -(i))
            
        return (-heapq.heappop(heap)-1) * (-heapq.heappop(heap)-1)
