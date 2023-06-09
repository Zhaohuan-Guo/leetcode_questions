# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre_node = None
        curr_node = head
        while curr_node:
            next_node = curr_node.next
            curr_node.next = pre_node
            pre_node = curr_node
            curr_node = next_node
        return pre_node