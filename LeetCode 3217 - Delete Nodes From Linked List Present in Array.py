"""     https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/solutions/5745368/python-beats-95-linked-list/     """



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        dummy = ListNode(0 , head)
        prev = dummy

        while prev.next:
            if prev.next.val in nums:
                prev.next = prev.next.next
            else :
                prev = prev.next
        return dummy.next
