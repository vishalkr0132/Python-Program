# using stack dsa insert total number of text books into a stack and take out the respective textbooks which is given by the user, if textbook is not present in the stack then return a message.
class Library:
    def __init__(self):
        self.queue = []
        self.temp = []
    
    def enqueue(self,book):
        self.queue[-1:] += [book]
        
    def dequeue(self):
        self.queue  = self.queue[1:]
        
    def find(self,book):
        if self.queue[0]==book:
            return self.queue.pop()
        else:
            for i in range(len(self.queue)):
                popped = self.queue.pop()
                self.temp[-1:] += [popped]
                if popped==book:
                    found = self.temp.pop()
                    while len(self.temp)!=0:
                        self.queue[-1:] += [self.temp.pop()]
                    return found
            else:
                return 'book does not exists'
    
    def display(self):
        return self.queue
            
lib = Library()
while True:
    print('1. Queue\n2. Dequeue\n3. Find a book\n4. Display\n5. Exit')
    match int(input('make your choice: ')):
        case 1:
            book = input('Enter the book name: ')
            lib.enqueue(book)
        case 2:
            lib.dequeue()
        case 3:
            book = input('Enter the book name: ')
            print(lib.find(book))
        case 4:
            print(lib.display())
        case 5:
             break
             
             
             
            