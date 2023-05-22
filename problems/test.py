from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        rs = []
        for i, num in enumerate(nums):
            nums[abs(num) - 1] = abs(nums[abs(num) - 1])*(-1)

        for i, num in enumerate(nums):
            if num > 0:
                rs.append(i + 1)
        return rs

s = Solution()
rs = s.findDisappearedNumbers([4,3,2,7,8,2,3,1])