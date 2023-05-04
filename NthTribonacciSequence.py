class Solution(object):
    def tribonacci(self, n):
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        seq = [0] * (n+1)
        seq[0], seq[1], seq[2], = 0, 1, 1

        for i in range(3,len(seq)):
            seq[i] = seq[i-1] + seq[i-2] + seq[i-3]

        return seq[n]