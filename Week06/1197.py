import sys

input = sys.stdin.readline

def find(parent, x):
    root = x
    while parent[root] != root:
        root = parent[root]
    while parent[x] != root:
        next_node = parent[x]
        parent[x] = root
        x = next_node
    return root

def union(parent, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)
    if rootA != rootB:
        if rootA < rootB:
            parent[rootB] = rootA
        else:
            parent[rootA] = rootB
        return True
    return False

V, E = map(int, input().split())
parent = [i for i in range(V + 1)]
edges = []

for _ in range(E):
    u, v, weight = map(int, input().split())
    edges.append((weight, u, v))

edges.sort()

total_weight = 0
edges_count = 0

for weight, u, v in edges:
    if union(parent, u, v):
        total_weight += weight
        edges_count += 1
        if edges_count == V - 1:
            break

print(total_weight)