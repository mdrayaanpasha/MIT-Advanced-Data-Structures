class PMachine:
    def __init__(self, max_num):
        self.b = BST()  
        self.n = None  
        self.max_num = max_num  

class PointerMachineHandler:
    def __init__(self, initial_limit):
        self.root = PMachine(initial_limit)
    
    def insert(self, key):
        temp = self.root
        prev = None
        
        while temp and temp.max_num < key:
            prev = temp
            temp = temp.n
        
        if not temp: 
            new_limit = prev.max_num
            while new_limit < key:
                new_limit *= 2
                new_node = PMachine(new_limit)
                prev.n = new_node
                prev = new_node
            temp = prev
        
        temp.b.insert(key)
    
    def search(self, key):
        temp = self.root
        while temp:
            if key <= temp.max_num:
                temp.b.search(key)
                return
            temp = temp.n
        print("Not found in any PMachine")

class Node:
    def __init__(self, data, left=None, right=None):
        self.d = data  
        self.l = left  
        self.r = right  

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        new_node = Node(key)
        
        if self.root is None:
            self.root = new_node
            return

        temp = self.root
        parent = None

        while temp:
            parent = temp
            if key < temp.d:
                temp = temp.l
            elif key > temp.d:
                temp = temp.r
            else:
                print("There is a duplicate node.")
                return

        if key < parent.d:
            parent.l = new_node
        else:
            parent.r = new_node
            
    def search(self, key):
        temp = self.root
        while temp:
            if temp.d == key:
                print("Found it!")
                return 
            elif key < temp.d:
                temp = temp.l
            else:
                temp = temp.r
                
        print("Not found!")


pm_handler = PointerMachineHandler(initial_limit=6)
pm_handler.insert(5)   
pm_handler.insert(10) 
pm_handler.insert(24)  

pm_handler.search(5)   
pm_handler.search(10)  
pm_handler.search(30)  
