class Node:
    def __init__(self, data, version):
        self.data = data
        self.next = None
        self.version = version

class FullyRetroActive:
    def __init__(self):
        self.root = None
        self.leaf = None
        self.versions = 0

    def _propagate_change(self, updated_node):
        temp = updated_node
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

    def insert(self, version, index, key, propagate=True):
        if version > self.versions or version < 0:
            print(f"No Can do: Version {version} isn't Available!")
            return
        
        temp = self.root
        while temp and temp.version != version:
            temp = temp.next

        if temp:
            temp.data.insert(index, key)
            if propagate:
                self._propagate_change(temp)
        else:
            print(f"No Can do: Version {version} isn't Available!")

    def delete(self, version, index, propagate=True):
        if version > self.versions or version < 0:
            print(f"No Can do: Version {version} isn't Available!")
            return
        
        temp = self.root
        while temp and temp.version != version:
            temp = temp.next

        if temp:
            temp.data.pop(index)
            if propagate:
                self._propagate_change(temp)
        else:
            print(f"No Can do: Version {version} isn't Available!")

fra = FullyRetroActive()
fra.insert_new_version([1, 2, 3])
fra.insert(0, 1, 4)
fra.delete(1, 0)
print(fra.root.data)
