# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        num = []
        head = ListNode()
        curr = head
        summation = 0
        while l1 or l2:
            if l1 and l2:
                summation += l1.val + l2.val
                l1 = l1.next
                l2 = l2.next
            elif l1:
                summation += l1.val
                l1 = l1.next
            elif l2:
                summation += l2.val
                l2 = l2.next


            if summation < 10:
                num.append(summation)
                summation = 0
            else:
                num.append(summation%10)
                summation = 1

        if summation == 1:
            num.append(1)

        for val in range(len(num)):
            curr.next = ListNode(num[val])
            curr = curr.next

        return head.next