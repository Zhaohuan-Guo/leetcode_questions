from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        rs = ''

        found_not_m = False  # 标志变量

        for i in range(1, len(strs[0])+1):
            for _ in range(1, len(strs)):
                if strs[0][:i] != strs[_][:i]:
                    found_not_m = True  # 设置标志变量为 True
                    break
                if _ == len(strs)-1:
                    rs = strs[0][:i]

            if found_not_m:
                    break  # 跳出整个循环




        return rs
solution = Solution()
rs = solution.longestCommonPrefix(["flower","flower","flower"])