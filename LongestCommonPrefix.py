class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 1:
            return strs[0]

        shortest = min(strs, key=len)

        for ch in range(len(shortest)):
            for word in strs:
                if word[ch] != shortest[ch]:
                    return word[:ch]

        return shortest