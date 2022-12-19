from collections import deque

N, M = map(int, input().split())
B = []
rx = 0
ry = 0
bx = 0
by = 0
for i in range(N):
    data = list(input().rstrip())
    B.append(data)
    for j in range(M):
        if data[j] == 'R':
            rx, ry = i, j
        if data[j] == 'B':
            bx, by = i, j

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()
queue.append((rx, ry, bx, by, 1))

visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]


def move(x, y, dx, dy):
    cnt = 0

    while B[x + dx][y + dy] != '#' and B[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt


while queue:
    go = 0
    rx, ry, bx, by, depth = queue.popleft()
    if depth > 10:
        break
    for i in range(4):
        nrx, nry, rcnt = move(rx, ry, dx[i], dy[i])
        nbx, nby, bcnt = move(bx, by, dx[i], dy[i])
        if B[nbx][nby] != 'O':
            if B[nrx][nry] == 'O':
                go = 1
                break
            if nrx == nbx and nry == nby:
                if rcnt > bcnt:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]

            if not visited[nrx][nry][nbx][nby]:
                visited[nrx][nry][nbx][nby] = True
                queue.append((nrx, nry, nbx, nby, depth + 1))
    if go == 1:
        print(depth)
        break

if go == 0:
    print(-1)