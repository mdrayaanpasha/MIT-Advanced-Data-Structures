class Node:
    def __init__(self, d, r=None, l=None):
        self.d = d
        self.r = r
        self.l = l
     
class BST:
    def __init__(self, root=None, ws_size=5):
        self.root = root
        self.ws = []
        self.ws_size = ws_size
    
    def insert(self, d):
        newNode = Node(d)
        if not self.root:
            self.root = newNode
            return
        
        temp = self.root
        parent = None
        
        while temp:
            parent = temp
            if temp.d > d:
                if not temp.l:
                    temp.l = newNode
                    return
                temp = temp.l
            elif temp.d < d:
                if not temp.r:
                    temp.r = newNode
                    return
                temp = temp.r
            else:
                print("Sorry mate, we got this in our BST already!")
                return
        
    def WSInsert(self, data):
        if len(self.ws) == self.ws_size:
            self.ws.pop(0)
        self.ws.append(data)
    
    def searchWithDynamicFinger(self, s):
        if s in self.ws:
            print("It exists in the working set!")
            return
        
        temp = self.root
        found = False
        while temp:
            if temp.d == s:
                found = True
                break
            elif temp.d > s:
                temp = temp.l
            else:
                temp = temp.r
                
        if found:
            print("We found it!")
            self.WSInsert(s)
        else:
            print("No can findsville babydoll")


bst = BST()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(7)
bst.insert(13)
bst.insert(17)

bst.searchWithDynamicFinger(7)
bst.searchWithDynamicFinger(100)
bst.searchWithDynamicFinger(10)
bst.searchWithDynamicFinger(15)
bst.searchWithDynamicFinger(13)
bst.searchWithDynamicFinger(5)
bst.searchWithDynamicFinger(7)  
