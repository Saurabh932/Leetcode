'''
    24. Swap Nodes in Pairs
    Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying
    the values in the list's nodes (i.e., only nodes themselves may be changed.)

    Example 1:

            Input: head = [1,2,3,4]
            Output: [2,1,4,3]

    Example 2:

            Input: head = []
            Output: []
'''


def swapPairs(head):
    # Base case: If head is None or there is only one node, return head
    if head is None or head.next is None:
        return head

    # Swap the first two nodes and recursively call swapPairs on the remaining list
    first = head
    second = head.next
    first.next = self.swapPairs(second.next)
    second.next = first

    # Return the new head of the modified list
    return second