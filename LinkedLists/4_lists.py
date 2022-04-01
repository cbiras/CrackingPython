"""
partition a singly linked list by a given value, 
such that the values smalled than the given one are in the left side of the list, while de bigger ones are in the right side

BONUS: keeps the order
"""
class ListNode(object):
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
def partition(head,x):
    left,right = ListNode(),ListNode()
    ltail,rtail = left,right

    while head:
        if head.val < x:
            ltail.next = head
            ltail = ltail.next
        else:
            rtail.next = head
            rtail = rtail.next
        head = head.next
    ltail.next = right.next
    rtail.next = None
    return left.next

if __name__=="__main__":
    head = ListNode(val=3,next=ListNode(val=5,next=ListNode(val=8,next=ListNode(val=5,next=ListNode(val=10,next=ListNode(val=2))))))
    x = 5
    head = partition(head,x)
    while head:
        print(head.val)
        head = head.next
