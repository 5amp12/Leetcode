class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        biggest = max(word1, word2, key=len)
        mergedString = ""
        for i in range(len(biggest)):
            if i > len(word1)-1:
                mergedString+=word2[i]
            elif i> len(word2)-1:
                mergedString+=word1[i]
            else:
                mergedString+=word1[i]
                mergedString+=word2[i]

        return mergedString