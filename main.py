from itertools import permutations
from sys import maxsize
v = 4
count = 0


def findShortestPath(distance):
    vertex = []

    for i in range(v):
        if i != count:
            vertex.append(i)

    min_value = maxsize
    next_permutation = permutations(vertex)

    for i in next_permutation:
        current_value = 0
        a = count
        for j in i:
            current_value += distance[a][j]
            a = j
        current_value += distance[a][count]
        min_value = min(current_value, min_value)
    return min_value


if __name__ == '__main__':
    distance = [[0, 10, 15, 20],
                [10, 0, 35, 25],
                [15, 35, 0, 30],
                [20, 25, 30, 0]]

    print(findShortestPath(distance))