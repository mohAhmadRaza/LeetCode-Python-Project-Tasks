class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        k -= 1
        L = list(range(1, n+1))
        q = deque(L)

        while len(q) != 1:
            q.rotate(-k)
            val = q.popleft()
        
        return q[0]
            

