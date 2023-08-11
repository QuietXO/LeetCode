# -*- coding: utf-8 -*-
"""
2. Add Two Numbers


You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""
import time


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


def list_to_node(lst):
    num = lst.pop(0)
    if lst:
        return ListNode(num, list_to_node(lst))
    return ListNode(num, None)


def print_node(node):
    cur = node
    lst = []
    while cur:
        lst.append(cur.val)
        cur = cur.next
    print(lst)


def main(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    dummy = cur = ListNode(0)
    rest = 0
    while l1 or l2 or rest:
        if l1:
            rest += l1.val
            l1 = l1.next
        if l2:
            rest += l2.val
            l2 = l2.next
        cur.next = ListNode(rest % 10)
        cur = cur.next
        rest //= 10
    return dummy.next


if __name__ == '__main__':
    node1 = list_to_node([9, 9, 9, 9, 9, 9, 9])
    node2 = list_to_node([9, 9, 9, 9])

    print_node(node1)
    print_node(node2)

    start_time = time.time()
    print(f'Final Number: {main(node1, node2).val}')
    print(f'--- {(time.time() - start_time)} seconds ---')

    print_node(main(node1, node2))
