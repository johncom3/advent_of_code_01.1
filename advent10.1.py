from collections import deque

with open("/Users/jonathanborer/Desktop/Programmieren WI/advent/advent_data/day10.txt") as fin:
    lines = fin.read().strip().split("\n")

n = len(lines)
m = len(lines[0])

# Time for graph shenanigans
# Construct adjacency graph

def get_nbrs(i, j):
    res = []
    for di, dj in get_dnbrs(i, j):  # Nutze nur die erlaubten Richtungen
        ii, jj = i + di, j + dj
        if 0 <= ii < n and 0 <= jj < m:  # Sicherstellen, dass der Nachbar im Gitter bleibt
            res.append((ii, jj))
    return res



def get_dnbrs(i, j):
    res = []
    if lines[i][j] == "S":
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ii, jj = i + di, j + dj
            if not (0 <= ii < n and 0 <= jj < m):
                continue

            if (i, j) in list(get_nbrs(ii, jj)):
                res.append((di, dj))
        return res

    else:
        res = {
            "|": [(1, 0), (-1, 0)],
            "-": [(0, 1), (0, -1)],
            "L": [(-1, 0), (0, 1)],
            "J": [(-1, 0), (0, -1)],
            "7": [(1, 0), (0, -1)],
            "F": [(1, 0), (0, 1)],
            ".": [],
        }[lines[i][j]]
        return res


si, sj = None, None
for i, line in enumerate(lines):
    if "S" in line:
        si, sj = i, line.index("S")
        break


# Do a BFS
visited = set()
dists = {}
q = deque([((si, sj), 0)])
while len(q) > 0:
    top, dist = q.popleft()
    if top in visited:
        continue
    visited.add(top)
    dists[top] = dist

    for nbr in list(get_nbrs(*top)):
        if nbr in visited:
            continue
        q.append((nbr, dist + 1))

ans = max(dists.values())
print(ans)