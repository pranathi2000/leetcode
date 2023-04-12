class Solution(object):
    def countAndSay(self, n):

        if n == 1:
            return "1"
        else:
            sequence = self.countAndSay(n-1)
            currNum = sequence[0]
            count = 0
            seq = ""
            for s in sequence:
                if s == currNum:
                    count+=1
                else:
                    seq = seq + str(count) + currNum
                    currNum = s
                    count = 1
            seq = seq + str(count) + currNum
            return seq


            