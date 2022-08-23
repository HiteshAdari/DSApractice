# Linked list implementation in Python


class Node:
    # Creating a node
    def __init__(self, item):
        self.item = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def insert(self, val, prev_node):
        val = Node(val)
        val.head = prev_node.next
        prev_node.next = val


if __name__ == '__main__':

    linked_list = LinkedList()

    # Assign item values
    linked_list.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = LinkedList()


    # Connect nodes
    linked_list.head.next = second
    second.next = third
    third.next = fourth
    fifth.insert(5,3)
    # Print the linked list item
    while linked_list.head != None:
        print(linked_list.head.item, end=" ")
        linked_list.head = linked_list.head.next
