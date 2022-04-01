""" find if a list has a cycle, and return the start of the loop"""
class ListNode(object):
    def __init__(self,val=0,next=None):
        self.val=val
        self.next = next
def findLoop(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    if not fast or not fast.next:
        return None
    
    slow = head
    while slow!=fast:
        slow = slow.next
        fast = fast.next
    return slow