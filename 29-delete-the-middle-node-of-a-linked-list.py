class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: ListNode) -> ListNode:
        
        if head.next is None:
            return None
        node = head
        delNode = head

        counter = 0
        while node is not None:
            counter +=1
            node = node.next
            
            

        for i in range((counter//2) - 1):    
            delNode = delNode.next
            

        delNode.next = delNode.next.next

        return (head)