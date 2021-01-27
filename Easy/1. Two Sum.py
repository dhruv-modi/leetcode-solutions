# https://leetcode.com/problems/two-sum/
    
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Constraints:

# 2 <= nums.length <= 103
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, num in enumerate(nums):
            dic[num] = i
        
        for i, num in enumerate(nums):
            a = target - num
            if a in dic and i != dic[a]:
                return [i, dic[a]]
            
