# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
         return None

        curr = head
        prev = None
        while curr is not None:
            next = curr.next
            curr.next = prev

            #DO NOT USE PARALLEL SWAPPING => WILL RESULT IN TOO MANY VALUES ERROR
            prev = curr
            curr = next

        head = prev

        return (head)