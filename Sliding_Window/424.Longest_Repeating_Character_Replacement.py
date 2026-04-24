class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        repeatedChars = {}
        longestString = 0
        for R in range(len(s)):
            if s[R] in repeatedChars:
                repeatedChars[s[R]] += 1
            else:
                repeatedChars[s[R]] = 1

            mostRep = max(repeatedChars, key=repeatedChars.get)
            mostRepVal = repeatedChars[mostRep]

            while ((R - L + 1) - mostRepVal) > k:
                repeatedChars[s[L]] -= 1
                L += 1
            
            longestString = max(longestString, (R-L)+1)
            
        return longestString
