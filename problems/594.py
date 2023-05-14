from typing import List

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        rs = 0
        hash_table = {}
        for num in nums:
            if num in hash_table:
                hash_table[num] += 1
            else:
                hash_table[num] = 1

        sorted_keys = sorted(hash_table.keys())
        for key in sorted_keys:
            if key+1 in hash_table:
                rs = max(rs, hash_table[key]+hash_table[key+1])

        return rs

solution = Solution()
rs = solution.findLHS([25202362,50490027,83368690,2520059,44897763,67513926,65180540,40383426,4089172,3455736])
print(rs)

'''
We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.

A subsequence of array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.

Input: nums = [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].
'''