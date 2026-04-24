class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        dash_count = 0
        count = 0
        for val in moves:
            if val is "L":
                count -= 1
            elif val is "R":
                count += 1
            else:
                dash_count += 1
        if count < 0:
            count -= dash_count
            count = -count
        else:
            count += dash_count
            
        return count