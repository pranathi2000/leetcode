class Solution(object):
    def lengthOfLongestSubstring(self, s):
        # ================
        # SLIDING WINDOW
        # ================
        
        leftWindow = 0
        seen = {}
        longest = 0
        if len(s) <= 1:
            return len(s)
        for right in range(len(s)):
            currChar = s[right]
            if seen.get(currChar) >= leftWindow :
                leftWindow = seen[currChar]+1
            seen[currChar] = right
            longest = max(longest, right-leftWindow+1)

        return longest

        # ================
        #   BRUTE FORCE
        # ================
        # longest = 0
        # if len(s) == 1:
        #     return 1
        # for i in range(len(s)):
        #     substring = ''
        #     for j in range(i,len(s)):
        #         if s[j] in substring:
        #             longest = max(longest, len(substring))
        #             break
        #         else:
        #             substring+=s[j]

        #     longest = max(longest, len(substring))

        # return longest

        # ================
        #   BRUTE FORCE
        # ================
        #         letterCount = {}
        #         if s[j] in letterCount:
        #             letterCount[s[j]]+=1
        #         else:
        #             letterCount[s[j]] = 1
        #         if letterCount[s[j]] > 1:
        #             if sum(letterCount.values())-1 > longest:
        #                 longest = sum(letterCount.values())-1
        #             letterCount = {}
        #             break