# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        if not head or not head.next:
            return
        
        a, b = self.split_list(head)
        
        b = self.reverse_list(b)
        
        self.merge_list(a, b)
        
    
    def split_list(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        

        nxt = slow.next
        slow.next = None
        return head, nxt
    
    def reverse_list(self, head):
        prev, curr, nxt = None, head, None
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev
    
    def merge_list(self, a, b):

        while a and b:
            a.next, a = b, a.next
            b.next, b = a, b.next
                    
