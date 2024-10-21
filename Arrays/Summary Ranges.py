class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        left, right = 0, 1

        res = []

        start = 0

        for i in range(1, len(nums)):
            if nums[i-1] + 1 == nums[i]:
                continue
            
            elif nums[i-1] == nums[i]:
                continue
            
            else:
                if start != i-1:
                   res.append(f'{nums[start]}->{nums[i-1]}')
                
                else:
                    res.append(f'{nums[start]}')
                
                start = i
        

        if start != len(nums)-1:
                   res.append(f'{nums[start]}->{nums[len(nums)-1]}')
                
        else:
            res.append(f'{nums[start]}')
        
        return res


