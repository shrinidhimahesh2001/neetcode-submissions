# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 is None:
            return list2

        if list2 is None:
            return list1

        # Make sure list1 starts with the smaller value
        if list2.val < list1.val:
            temp = list1
            list1 = list2
            list2 = temp

        head = list1
        prev = None

        while list1 is not None and list2 is not None:

            if list1.val <= list2.val:
                prev = list1
                list1 = list1.next

            else:
                next2 = list2.next

                prev.next = list2
                list2.next = list1

                prev = list2
                list2 = next2

        if list2 is not None:
            prev.next = list2

        return head  