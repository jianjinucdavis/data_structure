# node has data and next
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# a list of nodes
# head
'''API
x push_front(key)        add to front
x key top_front()        return front item
x pop_front()            remove front item
x push_back(key)         add to back
x top_back()             return back item
x pop_back()             remove back item
x boolean find(key)      is key in list
Erase(key)             remove key from list
boolean empty()        is list empty?
add_before(node, key)  add key before node
'''


class LinkedList:
    def __init__(self):
        self.head = None

    def empty(self) -> bool:
        return self.head is None

    def push_front(self, node: Node) -> None:
        if self.empty():
            self.head = node
        else:
            p = self.head
            self.head = node
            node.next = p

    def top_front(self) -> Node:
        return self.head

    def pop_front(self):
        # move head to next next
        if not self.empty():
            p = self.head
            if p.next:
                self.head = p.next
            # delete
            del p

    def push_back(self, node: Node):
        if self.empty():
            self.push_front(node)
        else:
            # go to the last node end
            p = self.head
            while p.next:
                p = p.next
            p.next = node

    def return_back(self) -> Node:
        if self.empty():
            return None
        else:
            p = self.head
            while p.next:
                p = p.next
            return p

    def pop_back(self):
        if not self.empty():
            p = self.head
            if not p.next:
                self.head = None
                del p
            else:
                lst = p.next
                while lst.next:
                    print(p.data)
                    p = p.next
                    lst = lst.next
                p.next = None
                del lst

    def find(self, key) -> bool:  # O(N)
        # if node in list, return True
        # else return False
        if not self.empty():
            p = self.head
            if p.data == key:
                return True
            while p.next:
                p = p.next
                if p.data == key:
                    return True
        return False

    def erase(self, key):
        if not self.empty():
            p = self.head
            # if first one matches
            if p.data == key:
                if p.next:
                    self.head = p.next
                    del p
                else:
                    del p
                    self.head = None
            while p.next:
                p = p.next
                if p.data == key:
                    if p.next:

                        self.head = p.next
                        del p
                    else:
                        del p


    def print(self):
        if not self.empty():
            p = self.head  # first node
            nodes = [p.data]
            while p.next:  # while it's not the last node
                p = p.next
                nodes.append(p.data)
            print('-->'.join([str(i) for i in nodes]))
        else:
            print("List is empty")


ll = LinkedList()
assert ll.empty(), True
ll.print()

ll.push_front(Node(1))
ll.print()
print('empty', ll.empty())

ll.push_front(Node(3))
ll.push_front(Node(5))
ll.push_front(Node(8))
print(ll.head.data)
print(ll.head.next.data)
print(ll.head.next.next.data)
print(ll.head.next.next.next.data)
ll.print()

ll.pop_front()
ll.print()

ll.push_back(Node(10))
ll.print()

t = ll.top_front()
print(t.data)
b = ll.return_back()
print(b.data)
print('====')
ll.print()
ll.pop_back()
ll.print()
print('find 3: ', ll.find(3))
print('find 1000: ', ll.find(1000))

'''
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)


ll.head = node1
node1.next = node2
node2.next = node3
node3.next = None
ll.tail = node3
print(ll.head.data)
print(ll.head.next.next.data)
'''
