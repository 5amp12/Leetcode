class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        longestPalLen = 1
        longestPal = s[0]
        for i in range(len(s)-1):
            for j in range(i+1, len(s)):
                if (s[i:j+1] == (s[i:j+1][::-1]) and j-i+1 > longestPalLen):
                    longestPal = s[i:j+1]
                    longestPalLen = j-i+1

        return longestPal