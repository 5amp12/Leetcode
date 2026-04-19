class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        closestNums = []
        for R in range(len(arr)):
            if len(closestNums) == k:
                closest = min(closestNums[0], arr[R], key=lambda num: abs(num - x))
                if closest == arr[R]:
                    closestNums.pop(0)
                    closestNums.append(arr[R])
                else:
                    break
            else:
                closestNums.append(arr[R])
        return closestNums