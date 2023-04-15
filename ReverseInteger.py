class Solution(object):
    def reverse(self, x):
        if x < 0:
            sign = -1
            x *= -1

        elif x > 0:
            sign = 1

        else:
            return 0

        reverse = 0

        while x > 0:
            reverse= (reverse*10) + (x%10)
            x = (x-(x%10)) // 10

        reverse *= sign

        if reverse > 2**31 - 1 or reverse < -1 * (2**31):
            return 0

        return reverse