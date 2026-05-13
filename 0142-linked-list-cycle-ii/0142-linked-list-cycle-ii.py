# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        slow= head
        fast= head
        while fast is not None and fast.next is not None:
            slow= slow.next
            fast= fast.next.next
            if slow==fast:
                pointer= head
                while slow != pointer:
                    pointer= pointer.next
                    slow= slow.next
                return slow
        return None