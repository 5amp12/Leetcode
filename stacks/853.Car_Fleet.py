class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = sorted(zip(position, speed))   #sorts only positions
        fleet = 0
        
        print(stack)

        prevToFinish = None
        for pos, spe in reversed(stack):
            hrsToFinish = (target - pos) / spe
            if prevToFinish is None or hrsToFinish > prevToFinish:
                prevToFinish = hrsToFinish
                fleet +=1
            stack.pop()

        #Finished in O(n)
        return fleet