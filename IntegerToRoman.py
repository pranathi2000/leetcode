class Solution(object):
    def intToRoman(self, num):
        symbols = [(1000,"M"), (900,"CM"), (500, "D"), (400,"CD"), (100,"C"), (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]

        symString = ""

        for i in range(len(symbols)):
            while num >= symbols[i][0]:
                num -= symbols[i][0]
                symString += symbols[i][1]

        return symString


        # First Approach Idea:
        # - Make a dictionary that contains all the mappings for symbol and value
        # ex. symbols = {1:"I", 4:"IV"......
        # - Make a while loop that repeats until num < 1
        # - In the while loop use 13 if statements to check if num is bigger than a number and
        # subtract that number from num and add the roman numeral associated to a string
