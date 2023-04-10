class Solution(object):
    def letterCombinations(self, digits):
        # =========================
        # SOLUTION 2 - BACKTRACKING
        # =========================
        mapping = {"2":"abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        if not digits:
            return []
        poss = []
        def backtracking(comb, d):
            if not d:
                poss.append(comb)
                return

            for l in mapping[d[0]]:
                backtracking(comb+l, d[1:])

        backtracking("", digits)
        return poss

        # ===============
        # SOLUTION 1
        # ===============
        # mapping = {"2":"abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        # poss = temp = []
        # for digit in digits:
        #     if not poss:
        #         poss = list(mapping[digit])
        #         continue
        #     for i in range(len(mapping[digit])):
        #        for j in range(len(poss)):
        #            temp.append(poss[j]+mapping[digit][i])
        #     poss = temp
        #     temp = []

        # return poss