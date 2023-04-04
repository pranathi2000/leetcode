class Solution:
    def twoSum(self, nums, target):
        m = {}

        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in m:
                return [m[comp], i]
            m[nums[i]] = i
        