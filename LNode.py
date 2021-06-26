class LNode:
    def __new__(self,x):
        self.data = x
        self.next = None

def Reverse(head):
    cur = None
    next = None

    cur = head.next.next
    head.next.next = None

    while cur is not None:
        next = cur.next
        cur.next = head.next
        head.next = cur
        cur = next
