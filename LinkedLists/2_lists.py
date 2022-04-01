""" return k-th to last elements to last
if k=2, just the last two element would be returned, while k=1 and k=0 returns the last element"""
class ListNode(object):
    def __init__(self,val=0,next=None):
        self.val=val
        self.next = next

#solution 1 is just printing, without returning the k-th to last elements, in a recursive manner
def kth_1(head,k):
    if not head:
        return 0
    index = kth_1(head.next,k) + 1
    if index == k:
        print(head.val)
    return index

"""solution 2 is using 2 pointers, iteratively.
First, move one pointer k-elements from the second pointer, then iterate with both pointers with the same step.
When the first pointer reaches the end, the second pointer is at k-th element"""

def kth_2(head, k):
    p1 = head
    p2 = head
    
    for i in range(k):
        if not p1:
            return None
        p1 = p1.next
    while p1:
        p1 = p1.next
        p2 = p2.next
    return p2

if __name__=="__main__":
    head = ListNode(val=1,next=ListNode(val=1,next=ListNode(val=2,next=ListNode(val=3,next=ListNode(val=4,next=ListNode(val=5))))))
    kth_1(head,3)
    sol_2 = kth_2(head,3)
    print(sol_2.val)
