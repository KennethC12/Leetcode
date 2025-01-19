# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Initialize the Pointers 
        slow = head
        fast = head

        

        while fast and fast.next: # The fast pointer moves two nodes while the slow pointer moves one
            slow = slow.next
            fast = fast.next.next

            if slow == fast: # So if the slow is == to fast that means it is in the linked list
                return True
        
        return False
