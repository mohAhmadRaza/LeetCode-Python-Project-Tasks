class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:    
        if start > destination:
            start, destination = destination, start
        
        total = sum(distance)
        clockwise = sum(distance[start:destination])
        anticlockwise = total - clockwise
        return min(clockwise, anticlockwise)

        
