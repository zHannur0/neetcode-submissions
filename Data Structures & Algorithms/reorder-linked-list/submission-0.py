# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        l1=head
        l2=head

        while l2 and l2.next:
            l1=l1.next
            l2=l2.next.next

        sec=l1.next
        l1.next=None

        halfR=None

        while sec:
            nextN=sec.next
            sec.next=halfR
            halfR=sec
            sec=nextN
            
        ans=head
        
        while halfR and ans:
            tmp1= ans.next
            tmp2=halfR.next

            ans.next=halfR
            halfR.next=tmp1

            ans=tmp1
            halfR=tmp2

        return None