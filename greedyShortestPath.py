class Node:
    def __init__(self, Name, Weight):
        self.Name = Name
        self.Connections = []  # Initialize an empty list for connections
        self.Weight = Weight

    def addConnection(self, Node, dist):
        self.Connections.append((Node, dist))


class Graph:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def algorithm(self):
        temp = self.start
        path = []
        total_distance = 0
        
        while temp is not None and temp.Name != self.end.Name:
            smallest = None
            min_distance = float('inf')
            
            for connection in temp.Connections:
                node, distance = connection
                if temp.Weight + distance < min_distance:
                    min_distance = temp.Weight + distance
                    smallest = node
            
            if smallest is None:
                break
            
            path.append(smallest.Name)
            total_distance += min_distance
            temp = smallest
        
        return path, total_distance


# Create nodes
Blr = Node('Bengaluru', 990)
Hyd = Node('Hyderabad', 710)
Maa = Node('Chennai', 1020)
Pun = Node('Pune', 150)
Mum = Node('Mumbai', 0)

# Add connections
Blr.addConnection(Maa, 1020)
Blr.addConnection(Hyd, 710)
Blr.addConnection(Pun, 150)

Hyd.addConnection(Pun, 540)

Maa.addConnection(Pun, 910)
Maa.addConnection(Hyd, 510)

Pun.addConnection(Mum, 150)

# Create graph and run algorithm
graph = Graph(Blr, Mum)
path, distance = graph.algorithm()

print(f"The shortest path from {graph.start.Name} to {graph.end.Name} is:\n {graph.start.Name} -> {' -> '.join(path)} \n with total distance {distance}")
