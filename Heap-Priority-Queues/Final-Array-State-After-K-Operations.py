class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        # Create a min-heap with tuples of (value, index)
        heap = [(nums[i], i) for i in range(len(nums))]
        heapq.heapify(heap)  # Transform list into a heap
        
        # Perform the operation for 'k' iterations
        for _ in range(k):
            num, ind = heapq.heappop(heap)  # Get the smallest element
            num *= multiplier  # Multiply the number by the multiplier
            heapq.heappush(heap, (num, ind))  # Push the modified number back into the heap
            nums[ind] = num  # Update the nums list with the new value at index 'ind'
        
        return nums
