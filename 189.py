"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
"""

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]
        return nums
    
nums = [1,2,3,4,5,6,7]
k = 3
print(Solution().rotate(nums, k)) # [5,6,7,1,2,3,4] 
        