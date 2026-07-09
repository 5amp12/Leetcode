class Solution:
    def sumAndMultiply(self, n: int) -> int:
        strN = ""
        
        listNum = []
        for num in str(n):
                if num != "0":
                        listNum.append(int(num))
                        strN += num
        
        if strN == "":
                return 0
        
        x = int(strN)
        sumx = sum(listNum)
        return sumx * x
        
                