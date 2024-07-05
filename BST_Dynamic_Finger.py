class Node:
    def __init__(self, d, r=None, l=None):
        self.d = d
        self.r = r
        self.l = l
        
class BST:
    def __init__(self, root=None):
        self.root = root
        
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
        
    def leftChildRotate(self, node):
        k = node.l
        node.l = k.r
        k.r = node
        return k
        
    def rightChildRotate(self, node):
        l = node.r
        node.r = l.l
        l.l = node
        return l
    
    def searchWithDynamicFinger(self, s):
        temp = self.root
        
        while temp and temp.d != s:
            if temp.d > s:
                temp = self.leftChildRotate(temp)
            else:
                temp = self.rightChildRotate(temp)
        
        if temp and temp.d == s:
            print("We found it!")
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
