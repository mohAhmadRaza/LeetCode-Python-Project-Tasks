class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity = sorted(capacity, reverse=True)
        total = sum(apple)
        n = len(capacity)

        current_capacity = 0

        for ind, cap in enumerate(capacity):
            current_capacity += capacity[ind]
            if  current_capacity >= total:
                return ind + 1
        
        return n
