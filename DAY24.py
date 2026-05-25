class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_sorted(self, data):
        new_node = Node(data)

        if self.head is None or data < self.head.data:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        while current.next and current.next.data < data:
            current = current.next

        new_node.next = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


def merge(head1, head2):
    

    dummy = Node(0)
    tail = dummy

    while head1 and head2:
        if head1.data <= head2.data:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next

        tail = tail.next

    
    if head1:
        tail.next = head1

    if head2:
        tail.next = head2

    return dummy.next


list1 = LinkedList()
list2 = LinkedList()


for value in [1, 3, 5, 7, 7]:
    list1.insert_sorted(value)

for value in [2, 3, 6, 7, 8]:
    list2.insert_sorted(value)

print("List 1:")
list1.display()

print("List 2:")
list2.display()

merged_head = merge(list1.head, list2.head)

print("Merged Sorted List:")
current = merged_head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")