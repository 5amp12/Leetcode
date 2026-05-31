class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids = sorted(asteroids)
        for i in range(len(asteroids)):
            if mass < asteroids[i]:
                return False
            mass+=asteroids[i]
        return True