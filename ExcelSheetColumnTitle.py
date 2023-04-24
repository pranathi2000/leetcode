class Solution(object):
    def convertToTitle(self, columnNumber):
        string = ''
        while columnNumber > 0:
            string+= chr(((columnNumber-1)%26) + ord('A'))
            columnNumber = ((columnNumber -1)//26)
        return string[::-1]