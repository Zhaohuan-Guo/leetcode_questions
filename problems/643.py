class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        curr_sum = sum(nums[0:k])
        max_avg = curr_sum / k

        for i in range(1, len(nums) - k + 1):
            curr_sum = curr_sum - nums[i - 1] + nums[i + k - 1]
            max_avg = max(max_avg, curr_sum / k)

        return max_avg


solution = Solution()
print(solution.findMaxAverage([0, 1, 1, 3, 3], 4))