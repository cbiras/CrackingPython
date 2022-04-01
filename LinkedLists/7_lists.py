""" find the point of intersection of two singly linked lists
easy solution is to save one list in a set, and to see if the second one has any intersection points
the hard one is to keep iterating through them, untill null or the point of intersection is reached
"""
class ListNode(object):
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next
def FindIntersection(head1,head2):
    l1,l2 = head1,head2
    while l1 != l2:
        l1 = l1.next if l1 else head2
        l2 = l2.next if l2 else head1
    return l1