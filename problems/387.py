class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_table = {}
        for i in s:
            if i not in hash_table:
                hash_table[i] = 1
            else:
                hash_table[i] += 1
        for i, char in enumerate(s):
            if hash_table[char] == 1:
                return i
        return -1

'''
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Input: s = "loveleetcode"
Output: 2
'''