class Solution(object):
    def titleToNumber(self, columnTitle):
        total = 0
        for letter in columnTitle:
            total = (total * 26) + (ord(letter)-(ord('A')-1))

        return total
