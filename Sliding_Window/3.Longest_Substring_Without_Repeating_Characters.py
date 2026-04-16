class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        currentString = []
        longestString = 0
        for letter in s:
            print(f"current string: {currentString}   current letter: {letter}")
                
            if letter in currentString:
                currentString = currentString[currentString.index(letter)+1:]
            currentString.append(letter)

            if len(currentString) > longestString:
                longestString = len(currentString)
            
        return longestString