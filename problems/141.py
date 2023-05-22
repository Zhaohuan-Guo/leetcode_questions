# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        count= 0
        node = head
        while not node:
            count += 1
            node.val = count
            if node.next.val < count:
                return True
            node = node.next
        return False

# 创建链表节点
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

# 构建普通链表
node1.next = node2
node2.next = node3
node

# 测试
solution = Solution()
result = solution.hasCycle(node1)
print(result)