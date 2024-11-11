'''Create a class with the name my_dictionary and when the object is created 
when should be create empty dictionary automatically.

it should contain a method like add items,display,delete items and modify items
'''

class my_dictionary:
    def __init__(self):
        self.d1 = {}
    
    def add_items(self, key, value):
        if key not in self.d1:
            self.d1[key] = value
        else:
            print(f"Key {key} already exists.")
            
    def display(self):
        print(self.d1)
        
    def delete_items(self, key):
        if key in self.d1:
            del self.d1[key]
        else:
            print(f"Key {key} does not exist.")
    
    def modify(self,key,value):
        if key in self.d1:
            self.d1[key] = value
        else:
            print(f"Key {key} does not exist.")
            

obj = my_dictionary()

obj.add_items('name', 'John')  
        
obj.add_items('age', 30)

obj.display()

obj.modify('age', 31)

obj.display()