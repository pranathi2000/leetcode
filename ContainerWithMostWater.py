class Solution(object):
    def maxArea(self, height):
        # TWO POINTERS
        maxArea, left, right = 0, 0, len(height)-1
        while right > left:
            maxArea = max(maxArea, min(height[left],height[right]) * (right-left))
            if height[right] > height[left]:
                left+=1
            else:
                right-=1
        return maxArea

        # BRUTE FORCE
        # maxArea = 0
        # for i in range(len(height)):
        #     for j in range(i+1, len(height)):
        #         maxArea = max(maxArea, min(height[i],height[j]) * (j-i))
        # return maxArea
