class Solution:
    def minElement(self, nums: List[int]) -> int:
        
        length = len(nums)
        arr = []
        heapq.heapify(arr)

        for i in range(length):
            ele = nums[i]
            ar = list(str(ele))
            s = sum(map(int, ar))
            heapq.heappush(arr, s)

        return arr[0]
