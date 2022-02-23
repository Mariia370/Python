n = int(input("Введите количество друзей: "))

my_graph = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(i+1, n):
        my_graph[i][j] = 1

print(*my_graph, sep='\n')
print(f'Количество рукопожатий: {sum([sum(i) for i in my_graph])}')

