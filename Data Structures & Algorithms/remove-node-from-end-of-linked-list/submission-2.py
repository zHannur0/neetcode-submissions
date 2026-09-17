# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)

        first = head

        for i in range(n):
            first = first.next

        dummy.next=head

        res=dummy
        while first:
            first=first.next
            dummy=dummy.next

        dummy.next=dummy.next.next

        return res.next