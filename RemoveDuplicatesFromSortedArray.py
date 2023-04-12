class Solution(object):
    def removeDuplicates(self, nums):
        previousNumIndex = 0
        for el in range(1,len(nums)):
            if nums[el] > nums[previousNumIndex]:
                nums[previousNumIndex + 1] = nums[el]
                previousNumIndex+=1

        return previousNumIndex+1

        