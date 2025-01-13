# Input: head = [0,1,2,3]

# Output: [3,2,1,0]


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        prev = None
        curr = head 
        while curr:
            nxt = curr.next    # temporarily store the next node
            curr.next = prev   # reverse the pointer
            prev = curr        # move `prev` one step forward
            curr = nxt         # move `curr` one step forward
        return prev