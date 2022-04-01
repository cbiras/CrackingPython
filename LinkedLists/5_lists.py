"""
having 2 lists, where each node represents 1 digit, sum the two lists and store the result in another linked list
"""
class ListNode(object):
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

def addLists(l1,l2,carry=0):
    if not l1 and not l2 and carry == 0:
        return None
    result = ListNode()
    value = carry
    if l1:
        value += l1.val
    if l2:
        value +=l2.val
    result.val = value %10

    if l1 or l2:
        more = addLists(l1 if l1 else None, l2 if l2 else None, 1 if value>=10 else 0)
        
        result.setNext(more)
    return result
