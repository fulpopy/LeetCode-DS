class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        slow = fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
            
            if slow is fast:
                return True
        return False
