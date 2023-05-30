'''
    1721. Swapping Nodes in a Linked List
    You are given the head of a linked list, and an integer k.

    Return the head of the linked list after swapping the values of the kth node from the beginning and
    the kth node from the end (the list is 1-indexed).

    Example 1:

            Input: head = [1,2,3,4,5], k = 2
            Output: [1,4,3,2,5]

    Example 2:

            Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
            Output: [7,9,6,6,8,7,3,0,9,5]
'''


def swapNodes(head, k):
    # Step 1: Find the length of the linked list
    length = 0
    curr = head
    while curr:
        length += 1
        curr = curr.next

    # Step 2: Initialize pointers
    first = None
    second = None

    # Step 3: Traverse to find the first node to swap
    curr = head
    for _ in range(k - 1):
        curr = curr.next
    first = curr

    # Step 4: Traverse to find the second node to swap
    curr = head
    for _ in range(length - k):
        curr = curr.next
    second = curr

    # Step 6: Swap the values of the nodes
    first.val, second.val = second.val, first.val

    return head

