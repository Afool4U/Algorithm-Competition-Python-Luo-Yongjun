N = 150
nodes = [0] * N

if __name__ == '__main__':
    n, m = map(int, input().split())
    for i in range(1, n):
        nodes[i] = i + 1
    nodes[n] = 1
    now, prev = 1, 1
    for _ in range(n - 1):
        for i in range(m - 1):
            prev = now; now = nodes[now]
        print(now, end=' ')
        nodes[prev] = nodes[now]
        now = nodes[prev]
    print(now)
