class Solution(object):
    def isPalindrome(self, x):
        # ==================
        # SOLUTION 3
        # ==================
        if x < 0:
            return False

        orig = x
        reverse = 0
        while orig > 0:
            reverse = reverse*10 + orig%10
            orig //= 10

        if x == reverse:
            return True

        return False





        # ==================
        # SOLUTION 2
        # ==================
        # if x < 0:
        #     return False

        # if x == 0:
        #     return True

        # reverse = 0
        # orig = x
        # power = int(floor(math.log(orig,10)))
        # print("POWER " + str(power))
        # while power >= 0:
        #     reverse += (orig%10)*(10**power)
        #     power-=1
        #     orig = orig //10
        #     print(reverse)

        # if x == reverse:
        #     return True
        # return False


        # ==================
        # SOLUTION 1
        # ==================
        # while x:
        #     print(x)
        #     if x%10 == x:
        #         return True
        #     elif x//10 == x%10:
        #         return True
        #     lastNum = x%10
        #     firstNum = x//10
        #     power = 1
        #     while firstNum >= 10:
        #         firstNum = firstNum//10
        #         power+=1
        #     if lastNum != firstNum:
        #         return False
        #     x = (x - (firstNum*(10**power)))//10

        # return True