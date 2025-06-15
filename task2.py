import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

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

def bfs_path(graph, start, goal):
    visited = set()
    queue = deque([[start]])

    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == goal:
            return path
        elif node not in visited:
            for neighbor in graph.neighbors(node):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
            visited.add(node)
    return None


def dfs_path(graph, start, goal):
    visited = set()
    stack = [[start]]

    while stack:
        path = stack.pop()
        node = path[-1]
        if node == goal:
            return path
        elif node not in visited:
            for neighbor in graph.neighbors(node):
                new_path = list(path)
                new_path.append(neighbor)
                stack.append(new_path)
            visited.add(node)
    return None

start_station = "Академмістечко"
end_station = "Червоний хутір"

path_bfs = bfs_path(G, start_station, end_station)
path_dfs = dfs_path(G, start_station, end_station)

print(f"\nШлях BFS від {start_station} до {end_station}:")
print(" → ".join(path_bfs))
print(f"Довжина шляху BFS: {len(path_bfs)-1}")

print(f"\nШлях DFS від {start_station} до {end_station}:")
print(" → ".join(path_dfs))
print(f"Довжина шляху DFS: {len(path_dfs)-1}")

print(f'Цікава ситуація, DFS і BFS знайшли шлях із 22 кроків, \
      але це не означає, що вони однаково працюють — але в даному конкретному графі так співпало.')
print('Висновок: 22 — це мінімально можливий шлях, тобто BFS зробив свою справу. А DFS випадково пішов «правильним» шляхом, який теж має 22 кроки.')