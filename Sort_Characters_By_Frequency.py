class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)

        heap = []

        for char, freq in c.items():
            heapq.heappush(heap, (-freq, char))
        
        string = []

        while heap:
            freq, char = heapq.heappop(heap)
            string.append(char * (-freq))
        
        return ''.join(string)
        
