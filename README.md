# Graph Traversal Algorithms in Python

## Breadth-First Search

File: `bfs.py`

### Input format

Input data must be in the following format

```
A B
City1 // Follows A lines each containing the name of a city
City2
City3
City4
...
CityV CityW // Follows B lines each containing a city pair
CityX CityY
...
```

Note that a single line `CityV CityW` means that it is possible to go from `CityV` to `CityW` and from `CityW` to `CityV`.

**Example:**

```
6 6
Tokyo
Kyoto
Niigata
Shizuoka
Nagoya
Toyama
Tokyo Niigata
Tokyo Shizuoka
Shizuoka Nagoya
Nagoya Kyoto
Toyama Niigata
Toyama Kyoto
```

### Usage

o run the program, use the following command: `python bfs.py <graph input file>`

The program will parse the given file and ask for a Start/Goal pair.
The program will then return the distance between the cities and the corresponding path.


**Example:**

```
$ python bfs.py inputBFS.txt 
Added city Tokyo
Added city Kyoto
Added city Niigata
Added city Shizuoka
Added city Nagoya
Added city Toyama
Added road Tokyo - Niigata
Added road Tokyo - Shizuoka
Added road Shizuoka - Nagoya
Added road Nagoya - Kyoto
Added road Toyama - Niigata
Added road Toyama - Kyoto
Nb Cities: 6, Nb Roads: 6
Graph: {'Toyama': ['Niigata', 'Kyoto'], 'Kyoto': ['Nagoya', 'Toyama'], 'Niigata': ['Tokyo', 'Toyama'], 'Tokyo': ['Niigata', 'Shizuoka'], 'Nagoya': ['Shizuoka', 'Kyoto'], 'Shizuoka': ['Tokyo', 'Nagoya']}
Please enter your start - goal:
> Tokyo Kyoto
Start: Tokyo
Destination: Kyoto
Computing distance and path from Tokyo to Kyoto
Connected roads for Tokyo:
        Road to Niigata
        Road to Shizuoka
Retrieved Tokyo
Retrieved Toyama
Retrieved Kyoto
Distance between Tokyo and Kyoto: 42 hops
Path:  ['Tokyo', 'Paris', 'Kyoto']
```

## Dijkstra

File: `dijkstra.py`

### Input format

Input data must be in the following format

```
A B
City1 // Follows A lines each containing the name of a city
City2
City3
City4
...
CityV CityW distanceVW  // Follows B lines each containing a city pair and the distance between them
CityX CityY distanceXY
...
```

Note that a single line `CityV CityW distanceVW` means that it is possible to go from `CityV` to `CityW` and from `CityW` to `CityV`.

**Example:**

```
6 6
Tokyo
Kyoto
Niigata
Shizuoka
Nagoya
Toyama
Tokyo Niigata 335
Tokyo Shizuoka 174
Shizuoka Nagoya 176
Nagoya Kyoto 195
Toyama Niigata 215
Toyama Kyoto 296
```

### Program usage

To run the program, use the following command: `python dijkstra.py <graph input file>`

The program will parse the given file and ask for a Start/Goal pair.
The program will then return the distance between the cities and the corresponding path.

**Example:**

```
$ python dijkstra.py input.txt 
Added city Tokyo
...
Added road Toyama - Kyoto: 296
Nb Cities: 6, Nb Roads: 6
Graph: {'Tokyo': {'Niigata': 335, 'Shizuoka': 174}, 'Niigata': {'Tokyo': 335, 'Toyama': 215}, 'Nagoya': {'Shizuoka': 176, 'Kyoto': 195}, 'Kyoto': {'Nagoya': 195, 'Toyama': 296}, 'Toyama': {'Niigata': 215, 'Kyoto': 296}, 'Shizuoka': {'Tokyo': 174, 'Nagoya': 176}}
Please enter your start - goal:
> Tokyo Kyoto
Start: Tokyo
Destination: Kyoto
...
Distance between Tokyo and Kyoto: 42
Path:  ['Tokyo', 'Paris', 'Kyoto']
```

_Note that the Dijkstra algorithm is not implemented and that the actual answer may differ._

## A*

The A* algorithm is very close to that of Dijkstra, but it uses additional information to guide the search to make it more efficient.
In this case, the GPS coordinates of the cities are used.

### Input format

Input data must be in the following format

```
A B
City1 lat1 long1 // Follows A lines each containing the name of a city and its latitude/longitute
City2 lat2 long2
City3 lat3 long3
City4 lat4 long4
...
CityV CityW distanceVW  // Follows B lines each containing a city pair and the distance between them
CityX CityY distanceXY
...
```

**Example:**

```
6 6
Tokyo 35.6895 139.6917
Kyoto 35.0116 135.7681
Niigata 37.9162 139.0364
Shizuoka 34.9756 138.3828
Nagoya 35.1815 136.9066
Toyama 36.6959 137.2137
Tokyo Niigata 335
Tokyo Shizuoka 174
Shizuoka Nagoya 176
Nagoya Kyoto 195
Toyama Niigata 215
Toyama Kyoto 296
```

### Usage 

Usage is the same as with Dijkstra. 