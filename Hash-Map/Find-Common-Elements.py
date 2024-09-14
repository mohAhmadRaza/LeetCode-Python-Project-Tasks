class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        nums1, nums2 = Counter(nums1), Counter(nums2)
        ans1, ans2 = 0, 0

        for a, b in nums1.items():
            if a in nums2.keys():
                ans1 += b
                ans2 += nums2[a]

        return [ans1, ans2] 
