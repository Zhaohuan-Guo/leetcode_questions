# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hash_table = {}
        node = head
        while node:
            if node.val not in hash_table:
                hash_table[node.val] = 1
            else:
                node.val = node.next.val
                node.next = node.next.next
        return head