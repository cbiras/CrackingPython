""" remove duplicates from an unsorted singly linked list"""

class ListNode(object):
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

def remove_duplicates(head):
    dup = set()
    prev = ListNode(-1)
    n = head
    while n:
        
        if n.val in dup:
            
            prev.next = n.next
        else:
            
            dup.add(n.val)
            prev = n
        
        n = n.next
    #print(head.val)
    return head

if __name__=="__main__":
    
    head = ListNode(val=1,next=ListNode(val=1,next=ListNode(val=2,next=ListNode(val=3,next=ListNode(val=4,next=ListNode(val=5))))))
    head = remove_duplicates(head)
    while head:
        print(head.val)
        head = head.next