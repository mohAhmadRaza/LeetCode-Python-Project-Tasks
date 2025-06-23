class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        length = len(candies)
        maximum = max(candies)

        arr = [True] * length

        for index, i in enumerate(candies):
            if i + extraCandies >= maximum:
                continue
            else:
                arr[index] = False
        
        return arr
