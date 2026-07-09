class Solution:
    def processStr(self, s: str) -> str:
        finalString = ""
        for letter in s:
            if letter.islower():
                finalString = finalString + letter
            elif letter == "*":
                finalString = finalString[:len(finalString)-1]
            elif letter =="#":
                finalString = finalString + finalString
            elif letter == "%":
                finalString = finalString[::-1]

        return finalString