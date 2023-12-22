from collections import deque

# Class implementing a FIFO (First-In First-Out) queue
# Add elements by calling `enqueue`
# Retrieve the element by calling `dequeue`
class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.empty():
            return self.queue.popleft()
        else:
            raise IndexError("Queue is empty")

    def empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

# Utility function used to parse the graph from a file and convert it to a useful data structure
# Returns a tuple with:
# - the number of cities in the graph
# - the number of roads in the graph
# - the graph
def parse_input(input_text):
    lines = input_text.strip().split('\n')
    citiesNb, roadNb = map(int, lines[0].split())
    
    # Extract the cities
    cities = set()
    for line in lines[1:1+citiesNb]:
        cities.add(line)
        print(f"Added city {line}")

    # Initialize an empty graph
    graph = {city: [] for city in cities}

    # Add the edges and the distances
    for line in lines[1+citiesNb:2+citiesNb+roadNb]:
        city1, city2 = line.split()

        # Add edges in both directions to the graph
        print(f"Added road {city1} - {city2}")
        graph[city1].append(city2)
        graph[city2].append(city1)

    return citiesNb, roadNb, graph


def bfs(graph, start, goal):
    print(f"Computing distance and path from {start} to {goal}")

    # TODO implement BFS algorithm and compute path from `start` to `goal`

    # Example of accessing the roads that a city is connected to:
    print(f"Connected roads for {start}:")
    
    # Iterate over connected cities and distances
    for neighbor in graph[start]:
        print(f"\tRoad to {neighbor}")

    # Example usage of priority queue
    queue = Queue()
    queue.enqueue('Tokyo')
    queue.enqueue('Toyama')
    queue.enqueue('Kyoto')
    while not queue.empty():
       # Elements are retrieved in the same order they were inserted
       node = queue.dequeue()
       print(f"Retrieved {node}")

    
    # Dummy values for return
    distance = 42
    path = [start, "Paris", goal]
    return distance, path



def main(filename):
    with open(filename, 'r') as file:
        input_text = file.read()

    A, B, graph = parse_input(input_text)
    print(f"Nb Cities: {A}, Nb Roads: {B}")
    print("Graph:", graph)


    start, goal = input("Please enter your start - goal:\n> ").split()

    # Print the received city names
    print(f"Start: {start}\nDestination: {goal}")

    # Check the cities are in the graph
    if start not in graph or goal not in graph:
        print("Error: Unknown city! Exiting...")
        sys.exit()

    # Call bfs to compute shortest path
    distance, path = bfs(graph, start, goal)

    print(f"Distance between {start} and {goal}: {distance} hops")
    print(f"Path: ", path)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python bfs.py input")
    else:
        main(sys.argv[1])







