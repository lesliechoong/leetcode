# Write an efficient program to find the sum of contiguous subarray within a one-dimensional array of numbers which has the largest sum.


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = curr = nums[0]
        for i in range(1, len(nums)):
            curr = max(nums[i], curr+nums[i])
            res = max(curr, res)
        return res
