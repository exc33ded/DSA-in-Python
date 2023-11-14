class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        # TODO
        if head is None:
            return head
        curr = dummy = ListNode(head.val)
        while head is not None:
            if head.val != dummy.val:
                dummy.next = ListNode(head.val)
                dummy = dummy.next
                head = head.next
            else:
                head = head.next
                    
        return curr
