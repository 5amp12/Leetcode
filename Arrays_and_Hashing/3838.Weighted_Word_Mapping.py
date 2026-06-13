class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        finalWord = ""
        for word in words:
            wordVal = 0
            for letter in word:
                wordVal += weights[ord(letter)-97]
            letterVal = wordVal % 26
            finalWord = finalWord + chr(122 - letterVal)

        return finalWord