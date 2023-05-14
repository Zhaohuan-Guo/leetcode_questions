class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        rs = 0
        while word*(1+rs) in sequence:
            rs += 1
        return rs

soluton = Solution()
rs = soluton.maxRepeating("aaabaaaabaaabaaaabaaaabaaaabaaaaba", 'aaaba')
print(rs)

'''
For a string sequence, a string word is k-repeating if word concatenated k times is a substring of sequence. The word's maximum k-repeating value is the highest value k where word is k-repeating in sequence. If word is not a substring of sequence, word's maximum k-repeating value is 0.
Given strings sequence and word, return the maximum k-repeating value of word in sequence.

Input: sequence = "ababc", word = "ba"
Output: 1
Explanation: "ba" is a substring in "ababc". "baba" is not a substring in "ababc".
'''