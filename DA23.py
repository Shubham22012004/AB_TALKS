class List:
    def __init__(self, number):
        self.number = number
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

    
    def add_List(self, number):
        new_list = List(number)

        if self.head is None:
            self.head = new_list
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = new_list

    
    def print_sll(self):
        temp = self.head

        while temp:
            print(f" {temp.number}", end="")

            if temp.next:
                print(" -> ", end="")

            temp = temp.next

        print()

    # Reverse linked list
    def reverse_sll(self):
        prev = None
        current = self.head

        while current:
            
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        
        self.head = prev



sll = SLL()


sll.add_List(1)
sll.add_List(2)
sll.add_List(3)
sll.add_List(4)

print("Original Train Order:")
sll.print_sll()

# Reverse linked list
sll.reverse_sll()

print("\nReversed SLL Order:")
sll.print_sll()