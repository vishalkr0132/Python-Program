class QUEUE:
    def __init__(self,maxSize):
        self.maxSize = maxSize
        self.Q = []
    def isFull(self):    
        if len(self.Q) == self.maxSize:
            return True
        else:
            return False
        
    def isEmpty(self):
        if len(self.Q) == 0:
            return True
        else:
            return False    
        
    def enqueue(self,val):
        if self.isFull():
            return 'Queue is full'
        else:
            self.Q.append(val) 
            
    def dequeue(self):
        if self.isEmpty():
            return 'Queue is empty'
        else:
            self.Q.pop(0)
    
    def display(self):
        if self.isEmpty():
            return 'Queue is empty'
        else:
            return self.Q
    
    def peek(self):
        if self.isEmpty():
            return 'Queue is empty'
        else:
            return self.Q[0]         

max_size = int(input('Enter the maximum size of the Queue: '))
que = QUEUE(max_size)  
        
while True:
    print('1.isFull\n2.isEmpty\n3.Enqueue\n4.Dequeue\n5.Display\n6.Peek\n7.Exit')                      
    match int(input('make your choice: ')):
        case 1:
            print(que.isFull())
            
        case 2:
            print(que.isEmpty())
            
        case 3:
            elem = int(input('Enter the elements: '))
            que.enqueue(elem)    
            
        case 4:
            que.dequeue()
            
        case 5:
            que.display()
            
        case 6:
            que.peek()     
        
        case 7:
            break
        
        case _:
            print('Invalid choice')           
                
