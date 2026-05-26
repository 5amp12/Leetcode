class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        letters = []
        numSpecialChar = 0
        for i in range(len(word)):
            if word[i] not in letters:
                letters.append(word[i])
        
        for i in range(len(letters)):
            if letters[i].isupper() and letters[i].lower() in letters:
                numSpecialChar += 1

        return numSpecialChar