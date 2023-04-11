class Solution(object):
    def combine(self, n, k):
        # BACKTRACKING
        
        c = []
        numRange = list(range(1,n+1))
        def backtrack(combination, numsLeft, numR):
            if numsLeft == 0:
                c.append(combination)
                return
            for x in numR:
                if x not in combination:
                    backtrack(combination+[x], numsLeft-1, numR[1:])
                else:
                    break

        backtrack([], k, numRange)
        return c