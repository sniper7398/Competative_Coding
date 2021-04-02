class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        temp = head
        slow = head
        fast = head
        while fast != None and fast.next != None:
            temp = slow
            slow = slow.next
            fast = fast.next.next
        
        temp.next = None
        left_side = self.sortList(head)
        right_side = self.sortList(slow)
        return self.mergsort(left_side,right_side)
    
    def mergsort(self, a, b):
        result = None
        if a == None:
            return b
        if b == None:
            return a
        
        if a.val<=b.val:
            result = a
            result.next = self.mergsort(a.next, b)
        else:
            result = b
            result.next = self.mergsort(a, b.next)
        return result    
