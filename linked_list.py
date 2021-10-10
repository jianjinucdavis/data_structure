import warnings

''' todo:
- doubly linked list
-- more efficient implementation
- algorithm practice
-- implement pydantic
'''


# node has data and next
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def empty(self) -> bool:
        return self.head is None

    def push_front(self, node: Node) -> None:
        if not isinstance(node, Node):
            print(f"instantiating Node({node})")
            node = Node(node)
        if self.empty():
            self.head = node
        else:
            p = self.head
            self.head = node
            node.next = p

    def top_front(self):
        return self.head.data

    def pop_front(self):
        # move head to next next
        if not self.empty():
            p = self.head
            if p.next:
                self.head = p.next
            else:
                self.head = None
            # delete
            del p
        else:
            warnings.warn("Empty List")

    def push_back(self, node: Node):
        if not isinstance(node, Node):
            print(f"instantiating Node({node})")
            node = Node(node)
        if self.empty():
            self.push_front(node)
        else:
            # go to the last node end
            p = self.head
            while p.next:
                p = p.next
            p.next = node

    def return_back(self):
        if self.empty():
            return None
        else:
            p = self.head
            while p.next:
                p = p.next
            return p.data

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
            # if erase first node
            if p.data == key:
                if p.next:
                    self.head = p.next
                    del p
                    return None
                else:
                    del p
                    self.head = None
                    return None
            # if erase second or later node: find node,
            while p.next:
                node1 = p
                node2 = p.next
                if node2.data == key:
                    # if node 2 is not the last node
                    # node1.next points to node2's next
                    # delete node2
                    if node2.next:
                        node1.next = node2.next
                        del node2
                        return None
                    # if node2 is the last node
                    else:
                        del node2
                        node1.next = None
                        return None

    def add_before(self, node, key):
        # add node before key
        if not isinstance(node, Node):
            print(f"instantiating Node({node})")
            node = Node(node)
        node1 = self.head
        if node1.data == key:
            self.head = node
            node.next = node1
        else:
            node2 = node1.next
            while node2.data != key:
                node1 = node1.next
                node2 = node2.next
            node1.next = node
            node.next = node2

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


class LinkedListTail(LinkedList):
    def __init__(self):
        self.head = None
        self.tail = None

    def push_front(self, node: Node) -> None:
        if not isinstance(node, Node):
            print(f"instantiating Node({node})")
            node = Node(node)
        if self.empty():
            self.head = node
            self.tail = node
        else:
            p = self.head
            self.head = node
            node.next = p

    def pop_front(self):
        # move head to next next
        if not self.empty():
            p = self.head
            if p.next:
                self.head = p.next
            else:
                self.head = None
                self.tail = None
            # delete
            del p
        else:
            warnings.warn("Empty List")

    def push_back(self, node: Node):
        if not isinstance(node, Node):
            print(f"instantiating Node({node})")
            node = Node(node)
        if self.empty():
            self.push_front(node)
        else:
            p = self.tail
            p.next = node
            self.tail = node

    def return_back(self):
        if self.empty():
            return None
        else:
            return self.tail.data

    def pop_back(self):
        if not self.empty():
            p = self.head
            if not p.next:
                self.head = None
                self.tail = None
                del p
            else:
                lst = p.next
                while lst.next:
                    print(p.data)
                    p = p.next
                    lst = lst.next
                p.next = None
                self.tail = p
                del lst

    def find(self, key) -> bool:  # O(N)
        # if node in list, return True
        # else return False
        if not self.empty():
            p = self.head
            if p.data == key:
                return True
            if self.tail.data == key:
                return True
            while p.next:
                p = p.next
                if p.data == key:
                    return True
        return False

    def erase(self, key):
        if not self.empty():
            p = self.head
            # if erase first node
            if p.data == key:
                if p.next:
                    self.head = p.next
                    del p
                    return None
                else:
                    del p
                    self.head = None
                    self.tail = None
                    return None
            # if erase second or later node: find node,
            while p.next:
                node1 = p
                node2 = p.next
                if node2.data == key:
                    # if node 2 is not the last node
                    # node1.next points to node2's next
                    # delete node2
                    if node2.next:
                        node1.next = node2.next
                        del node2
                        return None
                    # if node2 is the last node
                    else:
                        del node2
                        self.tail = node1
                        node1.next = None
                        return None


class DNode(Node):
    def __init__(self, data):
        super().__init__(data)
        self.prev = None

'''API
push_front(key)        add to front
key top_front()        return front item
pop_front()            remove front item
push_back(key)         add to back
return_back()             return back item
pop_back()             remove back item
boolean find(key)      is key in list
Erase(key)             remove key from list
boolean empty()        is list empty?
add_before(node, key)  add key before node
'''
class DoubleLinkedList(LinkedListTail):
    def push_front(self, node: DNode) -> None:
        if not isinstance(node, DNode):
            node = DNode(node)
        if self.empty():
            self.head = node
            self.tail = node
        elif self.head == self.tail:
            self.head = node
            node.next = self.tail
            self.tail.prev = node
        else:
            p = self.head
            self.head = node
            node.next = p
            p.prev = node
        return None

    def validate(self):
        if self.empty():
            print('VALIDATION: list empty')
            return None
        if self.head == self.tail:
            print('VALIDATION: list has 1 element')
            return None
        p = self.head
        head_list = list()
        head_list.append(p.data)
        while p.next:
            p = p.next
            head_list.append(p.data)
        t = self.tail
        tail_list = list()
        tail_list.append(t.data)
        while t.prev:
            t = t.prev
            tail_list.append(t.data)

        tail_list.reverse()
        if head_list != tail_list:
            raise Exception("List is not linked properly")
        else:
            print("VALIDATION PASSED")
            return None

    def print(self):
        if self.empty():
            print('EMPTY')
        elif self.head == self.tail:
            print('head-->', self.node.data, '-->tail')
        else:
            p = self.head
            data = list()
            data.append(p.data)
            while p.next:
                p = p.next
                data.append(p.data)
            print('HEAD seq')
            print("-->".join([str(d) for d in data]))
            t = self.tail
            data = list()
            data.append(t.data)
            while t.prev:
                t = t.prev
                data.append(t.data)
            print("TAIL seq")
            data.reverse()
            print("<--".join([str(d) for d in data]))

    def pop_front(self):
        if self.empty():
            return None
        elif self.head == self.tail:
            p = self.head
            self.head = None
            self.tail = None
            del p
            return None
        else:
            p = self.head
            self.head = p.next
            p.next.prev = None
            del p
            return None

    def pop_back(self):
        if self.empty():
            return None
        if self.head == self.tail:
            p = self.head
            del p
            self.head = None
            self.tail = None
            return None
        t = self.tail
        self.tail = t.prev
        t.prev.next = None
        del t
        return None

    def push_back(self, node: DNode):
        if not isinstance(node, DNode):
            node = DNode(node)
        if self.empty():
            self.head = node
            self.tail = node
        elif self.head == self.tail:
            self.head = node
            node.next = self.tail
            self.tail.prev = node
        else:
            t = self.tail
            self.tail = node
            node.prev = t
            t.next = node

    def erase(self, key):
        if self.empty():
            return None
        p = self.head
        if p.data == key:
            if p.next:
                self.head = p.next
                p.next.prev = None
            else:
                self.head = None
                self.tail = None
            del p
            return None
        while p.next:
            p = p.next
            if p.data == key:
                p.prev.next = p.next
                p.next.prev = p.prev
                del p
                return None

    def add_before(self, node: DNode, key):
        if not isinstance(node, DNode):
            node = DNode(node)
        if self.empty():
            return None
        else:
            p = self.head
            if p.data == node.data:
                self.push_front(DNode(key))
                return None
            while p.next:
                p = p.next
                if p.data == node.data:
                    pv = p.prev
                    n = DNode(key)
                    n.next = p
                    n.prev = pv
                    pv.next = n
                    p.prev = n
                    return None


'''
dl = DoubleLinkedList()
for i in range(5):
    dl.push_front(i)

dl.validate()
dl.print()
print(dl.top_front())
print('====')
dl.pop_front()
dl.print()
dl.pop_back()
dl.print()
dl.push_back(1000)
dl.validate()
dl.print()
print('===')
print(dl.top_front())
print(dl.return_back())
dl.erase(2)
dl.validate()
dl.print()
print('~~~~~')
dl.erase(3)
dl.validate()
dl.print()
dl.add_before(1, 0)
dl.validate()
dl.print()
dl.add_before(1000, 999)
dl.validate()
dl.print()
print('===')
edl = DoubleLinkedList()
edl.push_front(0)
edl.pop_front()
edl.print()
'''
