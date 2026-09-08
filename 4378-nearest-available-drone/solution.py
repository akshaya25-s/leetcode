class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        n = -1
        m = float('inf')
        for i, (x, y, r) in enumerate(drones):
            dx = abs(x - target[0])
            dy = abs(y - target[1])
            dist = dx + dy 
            
            if dist <= r and dist < m:
                m = dist
                n = i
        
        return n



