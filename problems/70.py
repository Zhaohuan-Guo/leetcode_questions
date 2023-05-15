class Solution:
    def climbStairs(self, n: int) -> int:
        a = 0
        b = 1
        rs = 0
        for i in range(n):
            rs = a + b
            a = b
            b = rs

        return rs