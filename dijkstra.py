import heapq

# Class implementing a priority queue
# Add elements by calling `put`
# Retrieve the element with the highest priority by calling `get`
class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, node, priority):
        heapq.heappush(self.elements, (priority, node))

    def get(self):
        return heapq.heappop(self.elements)

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
    graph = {city: {} for city in cities}

    # Add the edges and the distances
    for line in lines[1+citiesNb:2+citiesNb+roadNb]:
        city1, city2, distance = line.split()
        distance = int(distance)

        # Add edges in both directions to the graph
        print(f"Added road {city1} - {city2}: {distance}")
        graph[city1][city2] = distance
        graph[city2][city1] = distance

    return citiesNb, roadNb, graph


def dijkstra(graph, start, goal):
    print(f"Computing distance and path from {start} to {goal}")

    # TODO implement Dijkstra algorithm and compute path from `start` to `goal`

    # Example of accessing the roads that a city is connected to:
    print(f"Connected roads for {start}:")
    
    # Iterate over connected cities and distances
    for neighbor, distance in graph[start].items():
        print(f"\tRoad to {neighbor} with distance {distance}")

    # Example usage of priority queue
    pq = PriorityQueue()
    pq.put('Tokyo', 3.0)
    pq.put('Toyama', 1.0)
    pq.put('Kyoto', 2.0)

    while not pq.empty():
       node = pq.get()
       print(f"Retrieved {node[1]} with priority {node[0]}")

    
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

    # Call Dijkstra to compute shortest path
    distance, path = dijkstra(graph, start, goal)

    print(f"Distance between {start} and {goal}: {distance}km")
    print(f"Path: ", path)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python dijkstra.py input")
    else:
        main(sys.argv[1])







