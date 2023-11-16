class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def isPalindrome(self, head):
        # TODO
        
        # first, find the middle element
        slow = head
        fast = head
        
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        # second, reverse the other side of the linked list
        prev = None
        while slow:
            slow.next, prev, slow = prev, slow, slow.next
        
        # third, check equal condition and changes nodes
        while prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
            
            return True
            
