class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        print(new_node)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

   
        

# Creating a linked list of fruits
fruits_list = LinkedList()
fruits_list.append("Apple")
fruits_list.append("Orange")
fruits_list.append("Banana")
fruits_list.append("Grapes")

# Displaying the linked list

fruits_list.append("guava")

fruits_list.display()