class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = ""
        s1 = sorted(s1)
        for R in range(len(s2)):
            window += s2[R]
            if len(window) < len(s1):
                continue
            elif s1 == sorted(window):
                return True
            else:
                window = window[1:]

        return False
                