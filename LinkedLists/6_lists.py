"""
find if a linked list is a palindrome
Solution:
Reverse the last part of the linked list, and check if it is the same as the first part
"""
class ListNode(object):
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next
def pali(head):
    slow = fast = head
    
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    
    prev = None
    while slow:
        tmp = slow.next
        slow.next = prev
        prev = slow
        slow = tmp
    
    left,right = head,prev
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
    return True

if __name__=="__main__":
    head = head = ListNode(val=1,next=ListNode(val=2,next=ListNode(val=3,next=ListNode(val=3,next=ListNode(val=2,next=ListNode(val=69))))))
    print(pali(head))

