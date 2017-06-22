#!/usr/bin/env python

_author_ = "rifatul.islam"


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

    def Insert(head, data):

        node = Node(data=data, next_node=None)

        if head is None:
            head = node
            return head

        tail = head
        while tail.next is not None:
            tail = tail.next
        tail.next = node

        return head

    def Print(head):
        while head is not None:
            print(head.data)
            head = head.next

    def Insert_Head(head, data):
        node = Node(data=data, next_node=None)
        if head is None:
            head = node
            return head

        node.next = head
        return node

    def InsertNth(head, data, position):
        node = Node(data=data, next_node=None)

        if head is None:
            head = node
            return head

        if position == 0:
            node.next = head
            return node

        current_pos = 0
        while current_pos



