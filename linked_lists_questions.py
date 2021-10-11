from linked_list import LinkedList


''' Q1: 
Given a singly linked list and a position, 
delete a linked list node at the given position.

Input: position = 1, Linked List = 8->2->3->1->7
Output: Linked List =  8->3->1->7

Input: position = 0, Linked List = 8->2->3->1->7
Output: Linked List = 2->3->1->7
'''


def delete_index(ll: LinkedList, idx: int):
    if ll.empty():
        return None
    if idx < 0:
        return None
    p = ll.head
    cnt = 0
    if idx == cnt:
        # remove first
        ll.head = p.next
        p.next = None
        del p
        return None
    while p.next:
        p_prev = p
        p = p.next
        cnt += 1
        if cnt == idx: # delete p
            p_prev.next = p.next
            p.next = None
            del p
            return None
    if idx > cnt:
        print("idx not found")
        return None

'''
ll = LinkedList()
for i in range(5):
    ll.push_front(i)

ll.print()
delete_index(ll, 0)
ll.print()
delete_index(ll, 3)
ll.print()
ll.push_front(1000)
ll.print()
delete_index(ll, 1)
ll.print()

delete_index(ll, 5)
ll.print()
delete_index(ll, 2)
ll.print()
'''

''' Q2
Given a singly linked list. 
The task is to find the length of the linked list, 
where length is defined as the number of nodes in the linked list.
'''


def node_count(ll):
    cnt = 0
    p = ll.head
    if not p:
        return cnt
    while p.next:
        p = p.next
        cnt += 1
    return cnt

'''Q3 delete withuot head pointer
https://practice.geeksforgeeks.org/problems/delete-without-head-pointer/1/?category[]=Linked%20List&category[]=Linked%20List&page=1&query=category[]Linked%20Listpage1category[]Linked%20List#
'''
