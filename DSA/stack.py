'''
1. It is a linear, dynamic data structure works with the principle of "Frist in Last out" (FILO) or 
   "Last in First out" (LIFO)
2. To work on a stack we need to create a stack with the help of list in python datastructure
3. It can hold both homogenous and heterogenious data
'''
# syntax for creating a stack
# in this insertion and deletion of elements happen at the same end.
# we can have N number of elements in a stack data structure

# OPERATIONS :
# 1. push() : This method is used to add new element to the stack.
# 2. pop() : This method is used to remove the recently inserted element from the stack.
# 3. peek() : It returns the top most element in the stack.
# 4. isEmpty() : It returns true if stack does not contain any element else it returns false.
# 5. isFull() : It returns true if stack is reached its max size else it returns false.
# 6. display() : to display all the elements present in a stack.

class stack:
   def __init__(self, max_size):
      self.max_size = max_size
      self.stack = []
      
   def isEmpty(self):
      if len(self.stack) == 0:
         return True
      else:
         return False
      
   def isFull(self):
      if len(self.stack) == self.max_size:
         return True
      else:
         return False  
   
   def push(self,data):
      if self.isFull():
         print('\nThe stack is Full')
      else:
         self.stack.append(data)     
         
   def pop(self):
      if self.isEmpty():
         print('\nThe stack is empty')
      else:
         self.stack.pop()    
   
   def peek(self):           
      if self.isEmpty():
         print('\nThe stack is empty')
      else:
         print(f'\nThe last element of stack: {self.stack[-1]}')
   
   def display(self):
      print('\nElements inside the stack: ')
      for i in range(len(self.stack)-1,-1,-1):
         print(self.stack[i], end=' ') 
              
s = stack(int(input('max size of the stack: ')))      

while True:
   print('\n..............Stack Operations...............')
   print('\n1. 1sEmpty\n2. isFull\n3. push\n4. pop\n5. peek\n6. display\n7. Exit ')
   match int(input('make your choice: ')):
      case 1: s.isEmpty()
      case 2: s.isFull()
      case 3: s.push(int(input('Enter the value: ')))
      case 4: s.pop()
      case 5: s.peek()
      case 6: s.display()
      case 7: break   
      
  