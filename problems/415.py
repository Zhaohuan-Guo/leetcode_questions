class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        rs_list = []

        while i >= 0 or j >= 0 or carry > 0:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            current_sum = n1 + n2 + carry
            carry = current_sum // 10
            digit = current_sum % 10

            rs_list.append(str(digit))

            i -= 1
            j -= 1

        return ''.join(rs_list[::-1])



solution = Solution()
rs = solution.addStrings('9133', '87')
print(rs)