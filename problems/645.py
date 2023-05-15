from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        hash_table = [1]+[0]*len(nums)
        rs = [0, 0]
        for num in nums:
            hash_table[num] += 1
        for key, val in enumerate(hash_table):
            if val == 2:
                rs[0] = key
            elif val == 0:
                rs[1] = key
        return rs

'''
You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.
You are given an integer array nums representing the data status of this set after the error.
Find the number that occurs twice and the number that is missing and return them in the form of an array.

Input: nums = [1,2,2,4]
Output: [2,3]
'''

solution = Solution()
rs = solution.findErrorNums([1,2,2,4])
print(rs)
