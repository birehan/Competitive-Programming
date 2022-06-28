# Complete the has_cycle function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def has_cycle(head):
    next_node = head
    pre_node = head
    while next_node and next_node.next:
        next_node = next_node.next.next
        pre_node = pre_node.next
        if pre_node == next_node:
            return 1

    return 0