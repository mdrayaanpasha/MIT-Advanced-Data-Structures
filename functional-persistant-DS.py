class Node:
    def __init__(self, data, next_node, version):
        self.data = data
        self.next_node = next_node
        self.version = version


class FPDS:
    def __init__(self, root=None):
        self.root = root
        self.version = 0 if root is None else root.version

    def insert(self, data):
        self.version += 1
        new_node_data = self.root.data[:] if self.root else []
        new_node_data.append(data)
        new_node = Node(new_node_data, self.root, self.version)
        self.root = new_node

    def delete(self, index):
        if self.root and 0 <= index < len(self.root.data):
            self.version += 1
            new_node_data = self.root.data[:]
            new_node_data.pop(index)
            new_node = Node(new_node_data, self.root, self.version)
            self.root = new_node
        else:
            print("Index out of range!")

    def traverse_latest(self):
        if self.root:
            for i, item in enumerate(self.root.data):
                print(f"Task {i}: {item}")
        else:
            print("No data available.")

    def __str__(self):
        result = []
        temp = self.root
        while temp:
            version_info = f"Version {temp.version}: " + ", ".join(temp.data)
            result.append(version_info)
            temp = temp.next_node
        return "\n".join(result)


# Example usage
fpds = FPDS()
fpds.insert('Initial task')
fpds.insert('Task 1')
fpds.insert('Task 2')
fpds.delete(1)
print(fpds)
