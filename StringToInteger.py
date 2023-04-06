class Solution(object):
    def myAtoi(self, s):
        number=0
        s = s.strip()
        if not s:
            return 0
        sign = -1 if s[0] == '-' else 1
        s = s[1:] if s[0] in ['+','-'] else s
        for c in s:
            if c.isdigit():
                number = (number * 10) + int(c)
            else:
                break
            if number > (2**31) -1:
                if sign == -1:
                    return ((2**31)) * -1
                else:
                    return ((2**31)-1)
        return sign * number