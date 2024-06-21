import networkx as nx
import matplotlib.pyplot as plt
# Заданные рёбра графа в формате (вес, вершина1, вершина2)
edges = [(13, 1, 2), (18, 1, 3), (17, 1, 4), (14, 1, 5), (22, 1, 6),
         (26, 2, 3), (22, 2, 5), (3, 3, 4), (19, 4, 6)]

# Сортировка всех рёбер по весу
edges_sorted = sorted(edges, key=lambda x: x[0])
connected_vertices = set()  # Множество связанных вершин
group_mapping = {}  # Сопоставление вершины её группе
minimum_spanning_tree = []  # Минимальное остовное дерево

# Функция для получения группы вершины
def get_group(vertex):
    if vertex not in group_mapping:
        group_mapping[vertex] = [vertex]
    return group_mapping[vertex]

# Обход всех рёбер, строим минимальное остовное дерево с помощью алгоритма Краскала
for edge in edges_sorted:
    vertex1, vertex2 = edge[1], edge[2]
    group1 = get_group(vertex1)
    group2 = get_group(vertex2)

    if group1 != group2:
        minimum_spanning_tree.append(edge)  # Добавляем текущее ребро в остовное дерево
        new_group = group1 + group2
        for vertex in new_group:
            group_mapping[vertex] = new_group

print(minimum_spanning_tree)  # Выводим минимальное остовное дерево
# Создаем пустой граф
G = nx.Graph()

# Добавляем рёбра из исходного графа
for edge in edges:
    G.add_edge(edge[1], edge[2], weight=edge[0])

# Создаем пустой граф для минимального остовного дерева
T = nx.Graph()

# Добавляем рёбра из минимального остовного дерева
for edge in minimum_spanning_tree:
    T.add_edge(edge[1], edge[2], weight=edge[0])

# Расположение вершин на графике
pos = nx.spring_layout(G)

# Рисуем исходный граф
plt.figure(figsize=(12, 6))
plt.subplot(121)
nx.draw(G, pos, with_labels=True, node_size=1000, node_color='lightblue', font_weight='bold', font_size=10)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.title('Исходный граф')

# Рисуем минимальное остовное дерево
plt.subplot(122)
nx.draw(T, pos, with_labels=True, node_size=1000, node_color='lightgreen', font_weight='bold', font_size=10)
labels = nx.get_edge_attributes(T, 'weight')
nx.draw_networkx_edge_labels(T, pos, edge_labels=labels)

plt.title('Минимальное остовное дерево')

plt.tight_layout()
plt.show()