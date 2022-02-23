import random
from collections import deque

n = int(input("Введите количество вершин: "))
my_graph = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        my_graph[i][j] = random.randint(0, 2)


def dijkstra(graph, start):
    begin_from = start
    length = len(graph)
    is_visited = [False for _ in range(length)]
    cost = [float('inf') for _ in range(length)]
    parent = [-1 for _ in range(length)]
    cost[start] = 0
    min_cost = 0
    while min_cost < float('inf'):
        is_visited[start] = True
        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:
                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start
        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i

    result = [0 for _ in range(length)]
    for i in range(length):
        new_path = deque([i])
        finish = parent[i]
        if i == begin_from:
            finish = i
        else:
            while finish != begin_from:
                new_path.appendleft(finish)
                finish = parent[finish]
            new_path.appendleft(finish)
        result[i] = new_path
    return result

print("Таблица смежности графа:")
print(*my_graph, sep='\n')
print("Пути до каждой из вершин:")
answ = dijkstra(my_graph, 1)
for i in range(n):
    print(f'{i}: {list(answ[i])}')
