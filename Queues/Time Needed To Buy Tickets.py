class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        q = deque()
        count = 0
        n = len(tickets)
        seconds = 0
        for i, v in enumerate(tickets):
            q.append((v, i))
        
        value, ind = 0, 0

        while True:
            seconds += 1
            if q:
               value, ind = q.popleft()

            if value == 1 and ind != k and q:
                continue

            elif value == 1 and ind == k:
                break

            else:
                q.append((value-1, ind))
        
        return seconds
