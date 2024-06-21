class Vertex:
    def __init__(self,data,Next=None):
        self.data=data
        self.Next=Next
        
class PPDS:
    def __init__(self,root):
        self.root=root
    
    
    def insert(self,index,key):
        temp=self.root.data[:]
        temp.insert(index,key)
        
        new=Vertex(temp)
        new.Next=self.root
        self.root=new
        
    def deletion(self,index):
        temp=self.root.data[:]
        temp.pop(index)
        
        
        new=Vertex(temp)
        new.Next=self.root
        self.root=new
        
 
    
    def __str__(self):
        result = []
        current = self.root
        
        while current:
            result.append(" -> ".join(map(str, current.data)))
            current = current.Next
            
        return "\n".join(result)
      
            
            
sampleArr = [1, 5, 1, 4, 2, 5, 1]
rootVertex = Vertex(sampleArr)
PPDS = PPDS(rootVertex)

print("Initial version:\n", PPDS)

PPDS.insert(2, 10)
print("\nAfter insertion:\n", PPDS)

PPDS.deletion(3)
print("\nAfter deletion:\n", PPDS)
        
