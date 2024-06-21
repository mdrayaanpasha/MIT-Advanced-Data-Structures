class Vertex:
    def __init__(self,data,Next=None,version=0):
        self.data=data
        self.Next=Next
        self.version=version
        
class FPDS:
    def __init__(self,root,versions=0):
        self.root=root
        self.versions=versions
        
    def findVersion(self,v):
        temp=self.root
        
        while temp:
            if temp.version==v:
                return temp
            temp=temp.Next
        return None
        
    def insert(self,version,index,key):
        temp=self.findVersion(version)
        
        if not temp:
            raise ValueError(f"Version {version} not found")
        
        new_temp=temp.data[:]
        new_temp.insert(index,key)
        self.versions+=1
        new_vertex = Vertex(new_temp,temp.Next,self.versions)
        temp.Next=new_vertex
        
     
    def delete(self,version,index):
        temp=self.findVersion(version)
        if not temp:
            raise ValueError(f"Buddy we dont have version: ${version}")
            
        new_temp=temp.data[:]
        new_temp.pop(index)
        self.versions+=1
        new_vertex=Vertex(new_temp,temp.Next,self.versions)
        temp.Next=new_vertex
        
        
    def __str__(self):
        result = []
        current = self.root
        
        while current:
            result.append(f"Version {current.version}: " + " -> ".join(map(str, current.data)))
            current = current.Next
        
        return "\n".join(result)

# Example usage
sampleArr = [1, 5, 1, 4, 2, 5, 1]
rootVertex = Vertex(sampleArr)
FPDS = FPDS(rootVertex)

print("Initial version:\n", FPDS)

FPDS.insert(0, 2, 10)
print("\nAfter insertion:\n", FPDS)

FPDS.delete(1, 3)
print("\nAfter deletion:\n", FPDS)
        
        
            
