class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        t = {}

        for i in range(len(nums)):
            c = target - nums[i]
            if c in t:
                return [t[c], i]
            t[nums[i]] = i
