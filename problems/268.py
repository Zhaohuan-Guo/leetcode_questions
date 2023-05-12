class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        l = len(nums)
        return (1+l)*l//2-sum(nums)