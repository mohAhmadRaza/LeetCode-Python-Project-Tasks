class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        evens = [x for x in nums if x % 2 == 0]
        odds = [y for y in nums if y % 2 != 0]
        evens.extend(odds)
        return evens
