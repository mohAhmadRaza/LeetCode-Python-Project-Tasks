class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        for u, v, w in times:
            graph[u-1].append((v-1, w))

        distances = [float('inf')] * n
        distances[k-1] = 0

        priority_queue = [(0, k-1)]

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_distance < distances[current_node]:
                continue
            
            for neighbor, weight in graph[current_node]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
        
        s = max(distances)
        return s if s < float('inf') else -1
                
        
