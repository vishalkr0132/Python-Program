class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 

class Singly_Linked_List:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def display(self):
        """Display the linked list."""
        temp = self.head
        elements = []
        while temp:
            elements.append(temp.data)
            temp = temp.next
        return elements

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        """Push an element onto the stack."""
        self.stack.append(data)

    def pop(self):
        """Pop an element from the stack."""
        if self.is_empty():
            return None
        return self.stack.pop()

    def peek(self):
        """Peek the top element of the stack."""
        if self.is_empty():
            return None
        return self.stack[-1]

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0

    def display(self):
        """Display the stack."""
        return self.stack[::-1]  # Display in reverse order for stack view

# Main Code to Combine Singly Linked List with Stack
sll = Singly_Linked_List()
sll.insert_at_end(10)
sll.insert_at_end(20)
sll.insert_at_end(30)

print("Singly Linked List:", sll.display())

stack = Stack()
# Push all elements of the linked list to the stack
current = sll.head
while current:
    stack.push(current.data)
    current = current.next

print("Stack after inserting linked list:", stack.display())
