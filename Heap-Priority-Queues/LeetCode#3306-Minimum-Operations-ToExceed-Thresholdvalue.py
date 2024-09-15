class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # Edge case: if the list has less than 2 elements
        if len(nums) < 2:
            return 0 if nums and nums[0] >= k else -1
        
        count = 0
        heapq.heapify(nums)
        while nums[0] < k:
            a, b = heapq.heappop(nums), heapq.heappop(nums)
            heapq.heappush(nums, a*2+b)
            count += 1
        
        return count
