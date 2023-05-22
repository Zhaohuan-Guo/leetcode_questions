from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if not numRows:
            return []
        rs = [[1]]
        for i in range(1, numRows):
            rs.append([])
            rs[i].append(1)
            if i > 1:
                for j in range(i - 1):
                    rs[i].append(rs[i - 1][j] + rs[i - 1][j + 1])
            rs[i].append(1)

        return rs

solution = Solution()
rs = solution.generate(10)
print(rs)