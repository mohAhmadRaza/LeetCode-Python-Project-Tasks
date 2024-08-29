class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # Stroring the length of athelets's scores
        length = len(score)

        # Declared a queue to store medal's names
        q = deque(["Gold Medal","Silver Medal","Bronze Medal"])
        
        # Declared a heap queue to store scores in descending order
        heap = []
        
        # Initializing a list to store actual result
        result = [0] * length
        
        # Now pushing scores based on highest values in heap
        # Also pushing indexes to see where they are located originally
        for i in range(length):

            # Added '-' just for the sake of max heap pushing style
            heapq.heappush(heap, (-score[i], i))
        
        # ow reterivinf values from the heap
        for i in range(length):
            curr, ind = heapq.heappop(heap)

            # Checking if the queue has medals yet or not
            if q:

                # If queue yet has medals, give it to athlete and remove from queue
                result[ind] = q.popleft()
            
            # If no model found, means all medals used up for other athletes
            else:

                # Give athelete to their position based on their indexes, like '4th'
                result[ind] = str(i+1)
        
        return result
                


