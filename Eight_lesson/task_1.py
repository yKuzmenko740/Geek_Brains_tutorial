from collections import namedtuple

# обычный граф
graph1 = [
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 0],
    [0, 1, 0, 0]
]

print(*graph1, sep="\n")

print("*" * 50)
# ориентированый граф
graph2 = [
    [0, 1, 1, 0],
    [0, 0, 1, 1],
    [0, 1, 0, 0],
    [0, 0, 0, 0]
]

print(*graph2, sep="\n")

print("*" * 50)
# взвешаный граф
graph3 = [
    [0, 2, 3, 0],
    [0, 0, 2, 1],
    [0, 2, 0, 0],
    [0, 0, 0, 0]
]

print(*graph3, sep="\n")

print("*" * 50)
# списки смежности
graph4 = []
graph4.append([1, 2])
graph4.append([0, 2, 3])
graph4.append([0, 1])
graph4.append([1])

print(*graph4, sep='\n')

print("*" * 50)

graph5 = {
    0: {1, 2},
    1: {0, 2, 3},
    2: {0, 1},
    3: {1}
}
print(graph5)

if 3 in graph5[1]:
    print(True)

print("*" * 50)
# взвешаный граф + dict
Vertex = namedtuple("Vertex", ['vertex', 'edge'])
graph6 = []

graph6.append([Vertex(1, 2), Vertex(2, 3)])
graph6.append([Vertex(0, 2), Vertex(2, 2), Vertex(3, 1)])
graph6.append([Vertex(0, 3), Vertex(1, 2)])
graph6.append([Vertex(1, 1)])
print(*graph6, sep='\n')

for v in graph6[1]:
    if v.vertex == 3:
        print(True)


# graph in Class

class Graph:
    def __init__(self, vertex, edge, spam):
        self.vertex = vertex
        self.edge = edge
        self.spam = spam


# graph in list(edges)
graph_list = [(0, 1), (0, 2), (1, 2), (1, 3), (1, 3)]

print(*graph_list, sep="\n")


