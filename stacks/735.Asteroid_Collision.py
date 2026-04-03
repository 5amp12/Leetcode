class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for i in range(len(asteroids)):
            if asteroids[i] < 0:
                asteroidWeight = abs(asteroids[i])
                while stack and stack[-1] < asteroidWeight:
                    if stack[-1] < 0:
                        stack.append(asteroids[i])
                        break
                    stack.pop()
            
                if stack == []:
                    stack.append(asteroids[i])
                elif asteroidWeight == stack[-1]:
                    stack.pop()
                print (f"stack: {stack}")
                print(f"looking at {asteroids[i]}")
            else:
                stack.append(asteroids[i])
        
        return stack