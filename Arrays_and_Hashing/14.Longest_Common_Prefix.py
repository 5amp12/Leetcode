class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        def checkPrefix(prefix) -> bool:
            for x in range(1, len(strs)):
                if not strs[x].startswith(prefix):
                    return False

            return True

        prefix = ""
        for i in range(len(strs[0])):
            candidate = prefix + strs[0][i]
            if checkPrefix(candidate) :
                prefix += strs[0][i]
            else:
                break

        return prefix
