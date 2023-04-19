class Solution(object):
    def groupAnagrams(self, strs):
        ana = {}
        for s in strs:
            sortedWord = "".join(sorted(s))
            if sortedWord in ana:
                ana[sortedWord].append(s)
            else:
                ana[sortedWord] = [s]

        return ana.values()