class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        
        currBinary = 0
        res=[]

        for i in nums:
            currBinary = (currBinary * 2 + i) % 5
            res.append(currBinary == 0)
        
        return res
