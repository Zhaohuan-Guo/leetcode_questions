from collections import deque


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        queue = deque([])
        for char in s:
            queue.append(char)

        for char in t:
            if not queue:
                return True
            if char == queue[0]:
                queue.popleft()

        if not queue:
            return True
        else:
            return False

solution  = Solution()
rs = solution.isSubsequence('b', 'abc')
'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Input: s = "abc", t = "ahbgdc"
Output: true


'''