import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

station_pos = {
    "Академмістечко": (0, 9),
    "Житомирська": (1, 9),
    "Святошин": (2, 9),
    "Нивки": (3, 9),
    "Берестейська": (4, 9),
    "Шулявська": (5, 9),
    "Політехнічний інститут": (6, 9),
    "Вокзальна": (7, 9),
    "Університет": (8, 9),
    "Театральна": (9, 9),
    "Хрещатик": (10, 9),
    "Арсенальна": (11, 9),
    "Дніпро": (12, 9),
    "Гідропарк": (13, 9),
    "Лівобережна": (14, 9),
    "Дарниця": (15, 9),
    "Чернігівська": (16, 9),
    "Лісова": (17, 9),

    "Героїв Дніпра": (0, 6),
    "Мінська": (1, 6),
    "Оболонь": (2, 6),
    "Почайна": (3, 6),
    "Тараса Шевченка": (4, 6),
    "Контрактова площа": (5, 6),
    "Поштова площа": (6, 6),
    "Майдан Незалежності": (10, 6),
    "Площа Українських Героїв": (11, 6),
    "Олімпійська": (12, 6),
    "Палац Україна": (13, 6),
    "Либідська": (14, 6),
    "Деміївська": (15, 6),
    "Голосіївська": (16, 6),
    "Васильківська": (17, 6),
    "Виставковий центр": (18, 6),
    "Іподром": (19, 6),
    "Теремки": (20, 6),

    "Сирець": (2, 3),
    "Дорогожичі": (3, 3),
    "Лук'янівська": (4, 3),
    "Золоті ворота": (9, 3),
    "Палац спорту": (11, 3),
    "Кловська": (12, 3),
    "Печерська": (13, 3),
    "Звіринецька": (14, 3),
    "Видубичі": (15, 3),
    "Славутич": (16, 3),
    "Осокорки": (17, 3),
    "Позняки": (18, 3),
    "Харківська": (19, 3),
    "Вирлиця": (20, 3),
    "Бориспільська": (21, 3),
    "Червоний хутір": (22, 3)
}

lines = {
    "Червона": {
        "stations": [
            "Академмістечко", "Житомирська", "Святошин", "Нивки", "Берестейська",
            "Шулявська", "Політехнічний інститут", "Вокзальна", "Університет", 
            "Театральна", "Хрещатик", "Арсенальна", "Дніпро", "Гідропарк",
            "Лівобережна", "Дарниця", "Чернігівська", "Лісова"
        ],
        "color": "red",
        "times": [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    },
    "Синя": {
        "stations": [
            "Героїв Дніпра", "Мінська", "Оболонь", "Почайна", "Тараса Шевченка",
            "Контрактова площа", "Поштова площа", "Майдан Незалежності", "Площа Українських Героїв",
            "Олімпійська", "Палац Україна", "Либідська", "Деміївська", "Голосіївська",
            "Васильківська", "Виставковий центр", "Іподром", "Теремки"
        ],
        "color": "blue",
        "times": [2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    },
    "Зелена": {
        "stations": [
            "Сирець", "Дорогожичі", "Лук'янівська", "Золоті ворота", "Палац спорту",
            "Кловська", "Печерська", "Звіринецька", "Видубичі", "Славутич",
            "Осокорки", "Позняки", "Харківська", "Вирлиця", "Бориспільська", "Червоний хутір"
        ],
        "color": "green",
        "times": [2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3] 
    }
}

for line in lines.values():
    stations = line["stations"]
    color = line["color"]
    times = line["times"]
    for i in range(len(stations)):
        G.add_node(stations[i], pos=station_pos[stations[i]], color=color)
        if i < len(stations) - 1:
            G.add_edge(stations[i], stations[i+1], color=color, weight=times[i])

transfers = [
    ("Театральна", "Золоті ворота"),
    ("Хрещатик", "Майдан Незалежності"),
    ("Площа Українських Героїв", "Палац спорту")
]

for a, b in transfers:
    G.add_edge(a, b, color="black", weight=5)

pos = nx.get_node_attributes(G, 'pos')
colors = [G.nodes[n]['color'] for n in G.nodes]
edge_colors = [G.edges[e].get('color', 'gray') for e in G.edges]

pos_rotated = {node: (y, x) for node, (x, y) in pos.items()}

scale_factor = 1.2
pos_scaled = {node: (x * scale_factor, y * scale_factor) for node, (x, y) in pos_rotated.items()}


plt.figure(figsize=(8, 9))

nx.draw_networkx_nodes(G, pos_scaled, node_color=colors, node_size=100)
nx.draw_networkx_edges(G, pos_scaled, edge_color=edge_colors, width=2)

label_offset = 0.2
for node, (x, y) in pos_scaled.items():
    plt.text(x, y + label_offset, node, fontsize=10, ha='center', va='bottom')

edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos_scaled, edge_labels=edge_labels, font_size=7, label_pos=0.5)

plt.title("Карта Київського метро з часом руху", fontsize=16)
plt.axis('off')
plt.tight_layout()
plt.show()


num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degree_dict = dict(G.degree())
degrees = list(degree_dict.values())

min_degree = min(degrees)
max_degree = max(degrees)
avg_degree = sum(degrees) / len(degrees)

print(f"Кількість вершин (станцій): {num_nodes}")
print(f"Кількість ребер (з'єднань): {num_edges}")
print(f"Мінімальний ступінь вершини: {min_degree}")
print(f"Максимальний ступінь вершини: {max_degree}")
print(f"Середній ступінь вершини: {avg_degree:.2f}")

max_degree_nodes = [node for node, deg in degree_dict.items() if deg == max_degree]
print(f"Вершини з найбільшим ступенем ({max_degree}): {max_degree_nodes}")

print("\nСтупінь деяких станцій:")
sample_nodes = list(G.nodes)[:10]
for node in sample_nodes:
    print(f"{node}: {degree_dict[node]}")
