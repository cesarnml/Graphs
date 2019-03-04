"""
Simple graph implementation
"""


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return (len(self.queue))


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return (len(self.stack))


class Graph:
    """
    Represent a graph as a dictionary of vertices mapping labels to edges.
    """

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_directed_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist")

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
        else:
            raise IndexError("That vertex does not exist")

    def bft(self, starting_vertex_id):
        # Create an empty queue
        q = Queue()
        # Create an empty set of visited vertices
        visited = set()
        # Put the starting vertex in our Queue
        q.enqueue(starting_vertex_id)
        # While the queue is not empty....
        while q.size() > 0:
            # Dequeue the first node from the queue
            v = q.dequeue()
            # If that node has not been visited...
            if v not in visited:
                # Mark it as visited
                print(v)
                visited.add(v)
                # Then, put all of it's children into the queue
                for neighbor in self.vertices[v]:
                    q.enqueue(neighbor)

    def dft(self, starting_vertex_id):
        # Create an empty stack
        s = Stack()
        # Create an empty set of visited vertices
        visited = set()
        # Put the starting vertex in our Stack
        s.push(starting_vertex_id)
        # While the stack is not empty....
        while s.size() > 0:
            # Pop the top node from the stack
            v = s.pop()
            # If that node has not been visted...
            if v not in visited:
                # Mark it as visited
                print(v)
                visited.add(v)
                # Then, put all of it's children into the stack
                for neighbor in self.vertices[v]:
                    s.push(neighbor)

    def recursive_helper(self, vertex_id, visited):
        # Create a recursive_helper that adds current
        # vertex_id to visited set and prints vertex_id
        # Then for all vertex neighbors that have not been visited
        # Recursively call the recursive_helper
        visited.add(vertex_id)
        print(vertex_id)

        for v in self.vertices[vertex_id]:
            if v not in visited:
                self.recursive_helper(v, visited)

    def recursive_bft(self, starting_vertex_id):
        # Initiate visited set and call recursive helper on starting_vertex_id
        visited = set()
        self.recursive_helper(starting_vertex_id, visited)

    def bfs(self, start, goal):
        # Initialized visited set and array of paths
        visited = set()
        paths = [[start]]

        if start == goal:
            # If start = goal, return trivial path
            return paths[0]
        # Else depth-first-search all possible paths
        while paths:
            path = paths.pop(0)
            node = path[-1]
            # For latest node in current path
            if node not in visited:
                # If node not visited, iterate through neighbors
                # Appending each neighbor as next step in path
                neighbors = self.vertices[node]
                for neighbor in neighbors:
                    new_path = list(path)
                    new_path.append(neighbor)
                    paths.append(new_path)
                    # if neighbor is goal, return new_path
                    if neighbor == goal:
                        return new_path
                visited.add(node)
        # Visited all paths; no connecting route
        return 'No connecting path exist'

    def dfs(self, start, goal):
        # Analogues to bfs but paths are now accessed using FILO order
        visited = set()
        paths = [[start]]
        if start == goal:
            return paths[0]
        while paths:
            path = paths.pop()
            node = path[-1]
            if node not in visited:
                neighbors = self.vertices[node]
                for neighbor in neighbors:
                    new_path = list(path)
                    new_path.append(neighbor)
                    paths.append(new_path)
                    if neighbor == goal:
                        return new_path
                    visited.add(node)
        return 'no connecting path exist'


# TESTING
graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_vertex('4')
graph.add_vertex('5')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
graph.add_edge('3', '4')
graph.add_edge('4', '5')
graph.add_edge('1', '5')
print(graph.dfs('0', '5'))
