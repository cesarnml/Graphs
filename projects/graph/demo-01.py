class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty Queue
        q = Queue()
        # Create an empty Visited set
        visited = set()
        # Add the starting vertex to the queue
        q.enqueue(starting_vertex)
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first vertex
            v = q.dequeue()
            # If it has not been visited...
            if v not in visited:
                # Mark it as visited (print it and add it to the visited set)
                print(v)
                visited.add(v)
                # Then enqueue each of its neighbors in the queue
                for neighbor in self.vertices[v]:
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty Stack
        s = Stack()
        # Create an empty Visited set
        visited = set()
        # Push the starting vertex to the stack
        s.push(starting_vertex)
        # While the Stack is not empty...
        while s.size() > 0:
            # Pop the first vertex
            v = s.pop()
            # If it has not been visited...
            if v not in visited:
                # Mark it as visited (print it and add it to the visited set)
                print(v)
                visited.add(v)
                # Then push each of its neighbors onto the Stack
                for neighbor in self.vertices[v]:
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        # Mark the starting node as visited
        print(starting_vertex)
        visited.add(starting_vertex)
        # Call DFT_Recursive on each unvisited neighbors
        for neighbor in self.vertices[starting_vertex]:
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)
