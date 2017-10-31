"""
Homework 5 - Linked Lists

Release Date: 10-24
Due Date: 10-31 : s p o o k y :

To understand recursion, you must first understand recursion.
"""

class Node(object):
    """
    Class for linked list node.
    """
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

def list_length(head):
    if head is None:
        return 0
    return 1 + list_length(head.next_node)

def add_head(head, data):
    return Node(data, head)

    """
    Given the head of a linked list, appends the given element to
    the head.

    Input:
        head - the head of the linked list.
        data - the item to add to the head of the linked list.
    
    Output:
        the newly created linked list.
    """

def add_position(head, data, position):
    length = list_length(head)
    if position == 0:
        return Node(data,head)
    location = head
    previous = None
    temp = Node(data,None)
    for i in range(0, length):
        previous = location
        location = location.next_node
        if i == position:
            previous.next_node = temp
            temp.next_node = location
    if position >= length:
        endlocation = head
        for x in range(0, length):
            if x == length - 1:
                endlocation.next_node = Node(data, None)
            endlocation = endlocation.next_node
    return head
        
    """
    Given the head of a linked list, adds a new element so that
    it is at the given position. If the position is greater than
    the length of the linked list, place the new element at the end
    of the linked list.

    Input:
        head - the head of the linked list.
        data - the item to add to the linked list.
        position - the position to add the element in the linked list.
    Output:
        the head of the linked list.
    """
    pass

def remove_head(head):
    if head.data == None:
        return None
    return head.next_node
    """
    Given the head of a linked list, removes the first element.
    If head is None, returns None.

    Input:
        head - the head of the linked list.
    
    Output:
        the new head of the linked list.
    """
    pass

def remove_position(head, position):
    length = list_length(head)
    current = head
    previous = None
    if position == 0:
        return remove_head(head)
    for i in range(0, length):
        if i == position and position != 0:
            previous.next_node = current.next_node
        previous = current
        current = current.next_node
    return head
        
    """
    Given the head of a linked list, removes the element of the 
    specified position. If the position is greater than the length
    of the linked list, do not remove anything.

    Input:
        head - the head of the linked list.
        position - the position at which to remove an element.
    
    Output:
        the head of the linked list.
    """
    pass

def list_sum(head):
    sum = 0
    length = list_length(head)
    count = 0
    while count < length:
        sum += head.data
        head = head.next_node
        count += 1
    return sum
    """
    Given the head of a linked list with integer elements, returns
    the sum of the linked list.

    Input:
        head - the head of the linked list.
    
    Output:
        (int) the sum of the elements in the linked list.
    """
    pass

def is_merged(head_a, head_b):
    lengthA = list_length(head_a)
    lengthB = list_length(head_b)
    for i in range (0, lengthA):
        for x in range (0, lengthB):
            if head_a.data == head_b.data and head_a != None and head_b != None:
                return True
            
            head_b = head_b.next_node
        head_a = head_a.next_node
    return False
    """
    Given the heads of two linked lists, determines if the linked
    lists merge at some point.

    Input:
        head_a - the head of the first linked list.
        head_b - the head of the second linked list.
    
    Output:
        (bool) whether or not the linked lists merge.
    """
    pass

def find_merge_point(head_a, head_b):
    lengthA = list_length(head_a)
    lengthB = list_length(head_b)
    count = 0
    minValue = min(lengthA, lengthB)
    while count < minValue:
        if head_a.data == head_b.data:
            return head_a.data
        head_a = head_a.next_node
        head_b = head_b.next_node
        count += 1
    """
    Given the heads of two linked lists that merge, returns the
    data at that merge point.
    
    This will only be called on lists where
    is_merged(head_a, head_b) is true.

    Input:
        head_a - the head of the first linked list.
        head_b - the head of the second linked list.
    
    Output:
        the element at the merge point.
    """
    pass

def find_cycle(head):
    """
    Given the head of a linked list, determines whether or not there
    is a cycle in the linked list.

    Input:
        head - the head of the linked list.
    
    Output:
        (bool) whether or not there is a cycle in the linked list.
    """
    pass
