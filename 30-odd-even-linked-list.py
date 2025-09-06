class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        odd_ptr = head
        even_ptr = even_head = head.next

        while even_ptr and even_ptr.next:

            odd_ptr.next = even_ptr.next
            odd_ptr = odd_ptr.next
            
            even_ptr.next = odd_ptr.next
            even_ptr = even_ptr.next

        odd_ptr.next = even_head

        return (head)