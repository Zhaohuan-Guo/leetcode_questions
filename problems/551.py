class Solution:
    def checkRecord(self, s: str) -> bool:
        count = 0
        s_n = s + 'PP'
        for i, char in enumerate(s):
            if char == 'A':
                count += 1
                if count > 2:
                    return False
            elif char == 'L' and s_n[i+1] == 'L' and s_n[i+2] == 'L':
                return False
        return True

solution = Solution()
rs = solution.checkRecord('AA')
