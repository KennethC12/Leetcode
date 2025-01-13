# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        Merges two sorted linked lists and returns it as a new sorted list.
        The new list is made by splicing together the nodes of the first two lists.
        
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # Create a dummy node to serve as the start of the merged list
        dummy = ListNode()
        # 'node' will be used to track where we attach new nodes
        node = dummy

        # While both lists have nodes to process...
        while list1 and list2:
            # Compare the current nodes from both lists
            if list1.val < list2.val:
                # If list1's node value is smaller, attach it
                node.next = list1
                # Advance list1 to the next node
                list1 = list1.next
            else:
                # Otherwise, attach list2's node
                node.next = list2
                # Advance list2 to the next node
                list2 = list2.next
            
            # Move the 'node' pointer to the newly attached node
            node = node.next
        
        # At this point, one or both of the lists might still have nodes left
        # Attach whichever list is non-empty (or None if both are empty)
        node.next = list1 or list2

        # The merged list starts at dummy.next (dummy is just a placeholder)
        return dummy.next
