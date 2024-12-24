# It is a linear, dynamic data structure ted with the help of nodes and links
#  We can add N-Number of nodes to a single linked list with homogenious or heterogenious data

# Node : 
# It is a memory allocation to hold the data given by the user
# It contains TWO fields i. data and ii. address

class Node:
    def __init__(self,data):
        self.data = data
        self.add = None
        
# Head : We must have 'Head' node that holds all the nodes of SLL
# At first head node contains "None".
# When the nodes are created, Head node stores the address of the first node.
# Head always stores the address of the first node.

class Singly_Linked_List:
    def __init__(self):
        self.head = None
    
    
    # Insertion at last :
    # algorithm:
    # 1. create a new node
    # 2. check if the head node is None or contains some address
    # 3. if the head is None then assign the new node to the head
    # 4. If the head node has some address, then traverse upto the last node and then assign the new node to the address field of the last node.
    
    def Insert_at_Last(self,data):
        new_node = Node(data)   
        if self.head==None:
            self.head = new_node
            print('The head was None, head is created, now continue the insertion.')
        else:
            temp = self.head
            while temp.add:
                temp = temp.add
            temp.add = new_node
       
    # Display:
    # check if the head is None.
    # if the head is none return a message.
    # if head contains some address, traverse through all the nodes with temp node by printing the data inside the nodes.  
    
    def display(self):
        if self.head == None:
            print('The Linked List is empty')
        else:
            temp = self.head
            while temp!=None:
                print(temp.data,end='->')
                temp = temp.add
            print('None')   
            
    def length(self):
        if self.head==None:
            return 0
        else:
            temp = self.head
            count = 0
            while temp!=None:
                count += 1
                temp = temp.add
            return count         
    
    def Insert_at_First(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            new_node.add = self.head
            self.head = new_node   
    
    def At_location(self,loc,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            print('The head was None, head is created, now continue the insertion.')
        elif loc < 0:
            print('Invalid location!')
        elif loc == 1:
            self.Insert_at_First(data)
        elif loc > self.length():
            print('Invalid location!')
        else:
            temp = self.head
            count = 0
            while temp.add != None and count < loc-1:
                temp = temp.add
                count += 1
            
            new_node.add = temp.add
            temp.add = new_node
    def delete_at_last(self):
        if self    
                
                    
    # Deletions
    # 1. Deletion at last.
    
    
    
SLL = Singly_Linked_List() 
for i in range(2):
    SLL.Insert_at_Last(int(input('data: ')))
SLL.display()    
for i in range(4):
    SLL.Insert_at_First(int(input('data: ')))
SLL.display()    
SLL.At_location(4,100)
SLL.display()    
print(SLL.length())
            