# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        # For edge cases when you get an empty linked list or one with only one node
        if not head or not head.next:
            return head

        # Working in twos for switches
        second = head.next
        first = head
        head = second

        # 'prev' describes the node before the pair
        prev = None

        # This loop only works if there are two nodes in first and second
        # otherwise skips because list will be in order by then
        while first and second:
            # Makes switch in pairs and sets next node
            temp = second.next
            second.next = first
            first.next = temp

            # Sets previous pair secondary node to new first
            if prev:
                prev.next = second

            # Set new prev
            prev = first

            # Set new first and second
            first = temp
            if first:
                second = temp.next

        return head
