class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        #O(n(l))
        #For short form
        # count = Counter(text)
        # return min(count["b"], count["a"], count["l"] // 2, count["o"] // 2, count["n"])

        balloon_letter_store = {}
        for letter in text:
            if letter in "balloon":
                balloon_letter_store[letter] = balloon_letter_store.get(letter, 0) + 1
               

        numBalloons = 0
        while True:
            for balloon_letter in "balloon":
                if balloon_letter in balloon_letter_store and balloon_letter_store[balloon_letter] > 0:
                    balloon_letter_store[balloon_letter] -= 1
                else:
                    return numBalloons
            numBalloons +=1
        