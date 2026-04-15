class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0)   # fake start
        tail = dummy          # where we build the result

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1   # take from list1
                list1 = list1.next
            else:
                tail.next = list2   # take from list2
                list2 = list2.next

            tail = tail.next  # move forward

        # if something is left, attach it
        if list1:
            tail.next = list1
        else:
            tail.next = list2

        return dummy.next