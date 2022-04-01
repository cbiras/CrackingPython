"""
delete a node, when you only have acces to that node.
The node must must not be the head or the tail
"""
class ListNode(object):
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

#just copy the data from the next to the current, and delete the next
def delete_middle(node):
    if not node and not node.next:
        return False
    next = node.next
    node.val = next.val
    node.next = next.next
    return True
