import random


def create_graph(n):
    my_graph = []
    for i in range(n):
        number_of_vertices = random.randint(1, n)
        vertices = set()
        for _ in range(number_of_vertices):
            elem = random.randint(0, n - 1)
            if elem != i:
                vertices.add(elem)

        my_graph.append(list(vertices))

    return my_graph


def dfs(graph, start, the_next, finish, parents, is_visited):
    if not False in is_visited or the_next == -1:
        return "Нет пути"
    length = len(graph[the_next])
    print(start, the_next, finish, parents, is_visited)
    is_visited[the_next] = True
    flag = False
    for i in range(length):  # переходим на 1 вершину
        curr = graph[the_next][i]
        if not is_visited[curr]:
            flag = True

            is_visited[curr] = True
            parents[curr] = the_next
            the_next = curr

            break
    if finish == the_next:  # вершина найдена

        result = [finish, ]

        while parents[the_next] != start:
            result.append(parents[the_next])
            the_next = parents[the_next]
        result.append(start)
        return result[::-1]
    if not flag:
        # возврат назад

        return dfs(graph, start, parents[the_next], finish, parents, is_visited)
    return dfs(graph, start, the_next, finish, parents, is_visited)


n = int(input("Введите количество вершин: "))
graph = create_graph(n)
print("Списки смежности графа:")
for i in range(n):
    print(f'{i}: {graph[i]}')
s = int(input("Введите номер вершины, от которой ищем путь: "))
f = int(input("Введите номер вершины, к которой ищем путь: "))
is_visited = [False for _ in range(n)]
parents = [-1 for _ in range(n)]
print(f'Путь от вершины {s} до вершины {f}: {dfs(graph, s, s, f, parents, is_visited)}')
