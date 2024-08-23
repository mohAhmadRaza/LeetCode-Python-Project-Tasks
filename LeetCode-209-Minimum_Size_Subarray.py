class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        # Making two pointers, on of them will be at the start
        # Seond one will be at the end
        left, right = 0, 0

        # Initially we have first element as the sum
        currSum = nums[0]

        # Initially minimum length is in infinity
        minimum = float('inf')
        
        # run this loop until we have not an ending point
        while right <= len(nums)-1:

            # If current sum is less than target
            if currSum < target:

                # Increment the right pointer
                right += 1

                # if right pointer is not out of index
                if right <= len(nums) - 1:

                    # Add it to the currenSum
                    currSum += nums[right]
            
            # If currentSum is greater than target
            else:

                # Choose minimum from the previous and this new value
                minimum = min(minimum, right - left + 1)

                # Increment left pointer
                currSum -= nums[left]
                left += 1
        
        return minimum if minimum != float('inf') else 0
                
