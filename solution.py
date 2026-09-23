class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_nums = 0
        for i in range(len(nums)):
            if i > max_nums:
                return False
            max_nums = max(max_nums, i+nums[i])
             
        return True
