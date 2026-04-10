# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:
import math
class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 0, n
        
        while l <= r:
            middle = (l + r) // 2
            apiRet = guess(middle)
            if apiRet == -1:
                r = middle - 1
            elif apiRet == 1:
                l = middle + 1
            else:
                return middle
            print(middle)
        return l

           
        