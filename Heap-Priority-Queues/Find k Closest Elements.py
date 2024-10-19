class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []

        for i in arr:
            heapq.heappush(heap, (abs(i - x), i))
        
        res = [0] * k

        for i in range(k):
            sums, ele = heapq.heappop(heap)
            res[i] = ele
        
        res.sort()
        return res
