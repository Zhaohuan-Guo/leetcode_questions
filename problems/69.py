class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        x_n = x
        while x_n ** 2 - x > 0.1:
            x_n = (x_n + x / x_n) / 2

        return int(x_n)


solution = Solution()
rs = solution.mySqrt(36)
print(rs)