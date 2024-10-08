class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)
        stack = []

        hashMap = {n : i for i, n in enumerate(nums1)}

        for i in nums2:
            while stack and stack[-1] < i:
                smaller = stack.pop()
                if smaller in hashMap:
                    res[hashMap[smaller]] = i
            
            stack.append(i)
        
        return res
