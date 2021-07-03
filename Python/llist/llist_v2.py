class LList:
    """
    Single Linked List
    """
    @staticmethod
    def init(lst):
        if len(lst) == 0:
            return None
            
        head = LListNode(None)
        node = head
        for (i, x) in enumerate(lst):
            node.val = x
            if(i is not len(lst) - 1):
                node.next = LListNode(None)
                node = node.next
        return head

    @staticmethod
    def display(head):
        node = head
        result = str(node.val)
        while node.next:
            node = node.next
            result += ', {}'.format(node.val)
        print(result)
        return None
        
    @staticmethod
    def reverse(head):
        '''
        1. set var for prev_node, node and next_node
        2. while loop each node
            2.1. change direction
            2.2. move on nodes
        '''
        # 1. set var for prev_node, node and next_node
        result = head
        node = head
        prev_node = None
        next_node = None
        
        while node is not None:
            # 2.1. change direction
            next_node = node.next
            node.next = prev_node
            
            # 2.2. move on nodes
            prev_node = node
            node = next_node
            result = prev_node
            
        return result

        
class DLList(LList):
    """
    Double Linked List
    """
    @staticmethod
    def init(lst):
        if len(lst) == 0:
            return None
            
        head = DLListNode(None)
        tail, node = head, head
        prev_node, next_node = None, None
        
        for (i, x) in enumerate(lst):
            node.val = x
            node.prev = prev_node
            if(i is not len(lst) - 1):
                next_node = DLListNode(None)
            else:
                next_node = None
                tail = node
            
            node.next = next_node
            prev_node = node
            node = node.next
            
        return head, tail
    
    @staticmethod
    def reverse(head):
        tail = head
        node = head
        prev_node = None
        next_node = None
        
        while node is not None:
            next_node = node.next
            node.next = prev_node
            node.prev = next_node
            head = node
            prev_node = node
            node = next_node
            if next_node is not None:
                next_node = next_node.next
            
        return head, tail



class CLList(LList):
    @staticmethod
    def init(lst):
        if len(lst) == 0:
            return None
            
        head = LListNode(None)
        node = head
        for (i, x) in enumerate(lst):
            node.val = x
            if(i is not len(lst) - 1):
                node.next = LListNode(None)
                node = node.next
            else:
                node.next = head

        return head

    @staticmethod
    def display(head):
        if not head:
            return None

        node = head
        result = str(node.val)

        if not node.next: # case 1 node
            print(result)
            return None

        slow = node.next
        fast = node.next.next

        while fast != slow:
            result += ', {}'.format(slow.val)
            slow = slow.next
            fast = fast.next.next

        print(result)

        return None


        
    @staticmethod
    def reverse(head):
        #    [1] -> [2] -> [3] -> [4]
        #(1) prev,  curt   
        #(2)        prev,  curt
        #(3)               prev,  curt
        #(4) curt,                prev
        if not head:
            return None

        if not head.next:
            return head

        prev_node = None
        node = head
        next_node = node.next

        while True:
            prev_node = node
            node = next_node
            next_node = next_node.next
            node.next = prev_node

            if node == head:
                break

        return head


class LListNode:
    '''
    for node structure in linked list
    '''
    def __init__(self, val):
        self.val = val
        self.next = None
        
    def __str__(self):
        if self.val:
            return self.val
        return ''


class DLListNode(LListNode):
    '''
    for node structure in double linked list
    '''
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    """
    For (Single) Linked List
    """
    print("===== (Single) Linked List =====")
    head = LList.init(lst)
    LList.display(head) # 1, 2, 3, 4, 5, 6, 7, 8, 9
    new_head = LList.reverse(head)
    LList.display(new_head) # 9, 8, 7, 6, 5, 4, 3, 2, 1
    
    """
    For Double Linked List
    """
    print("===== Double Linked List =====")
    head, tail = DLList.init(lst)
    DLList.display(head) # 1, 2, 3, 4, 5, 6, 7, 8, 9
    new_head, new_tail = DLList.reverse(head)
    DLList.display(tail) # 9, 8, 7, 6, 5, 4, 3, 2, 1

    """
    For Circle (Single) Linked List
    """
    print("===== Circle (Single) Linked List =====")
    head = CLList.init(lst)
    CLList.display(head) # 1, 2, 3, 4, 5, 6, 7, 8, 9
    new_head = CLList.reverse(head)
    CLList.display(new_head) # 1, 9, 8, 7, 6, 5, 4, 3, 2