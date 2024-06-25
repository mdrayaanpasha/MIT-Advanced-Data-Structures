class Node:
    def __init__(self, data, version):
        self.data = data
        self.next = None
        self.version = version

class PartialRetroActive:
    def __init__(self):
        self.root = None
        self.leaf = None
        self.versions = 0

    def insert(self, index, key, version):
        if version > self.versions or version < 0:
            print("No can do: Version", version, "isn't available!")
            return
        
        temp = self.root
        while temp and temp.version != version:
            temp = temp.next
            
        if temp is None:
            print("Version", version, "not found!")
            return

        temp.data.insert(index, key)
        self._propagate_changes(temp)

    def delete(self, version, index):
        if version > self.versions or version < 0:
            print("No can do: Version", version, "isn't available!")
            return
        
        temp = self.root
        while temp and temp.version != version:
            temp = temp.next
            
        if temp is None:
            print("Version", version, "not found!")
            return

        temp.data.pop(index)
        self._propagate_changes(temp)

    def _propagate_changes(self, start_node):
        temp = start_node
        while temp:
            if temp.next:
                temp.next.data = temp.data[:]
            temp = temp.next

    def insert_new_version(self, new_data):
        new_node = Node(new_data, self.versions)
        
        if self.root is None:
            self.root = new_node
            self.leaf = new_node
        else:
            self.versions += 1
            new_node.version = self.versions
            self.leaf.next = new_node
            self.leaf = new_node

    def get_version(self, version):
        if version > self.versions or version < 0:
            print("No can do: Version", version, "isn't available!")
            return None
        
        temp = self.root
        while temp and temp.version != version:
            temp = temp.next
            
        return temp.data if temp else None

# Example usage
pra = PartialRetroActive()
initial_data = [1, 2, 3]
pra.insert_new_version(initial_data)
pra.insert(2, 4, 0)
pra.delete(1, 1)  
print(pra.get_version(0))  
print(pra.get_version(1)) 
