class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_table = {}
        for i, num in enumerate(nums):
            if num in hash_table and i - hash_table[num] <= k:
                return True
            hash_table[num] = i
        return False

'''
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
Input: nums = [1,2,3,1], k = 3
Output: true
'''