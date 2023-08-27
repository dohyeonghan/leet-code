# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        head_list: List = []
        
        while head.next is not None:
            head_list.append(head.val)
            head = head.next
        head_list.append(head.val)
        
        while len(head_list) > 1:
            if head_list.pop(0) != head_list.pop(-1):
                return False
        return True
            
            

