N = 105


class Node:
    id, next_id = None, None
    # data = None


nodes = [Node() for _ in range(N)]

if __name__ == '__main__':
    n, m = map(int, input().split())
    nodes[0].next_id = 1
    for i in range(1, n + 1):
        nodes[i].id = i
        nodes[i].next_id = i + 1
        next_id = i + 1
    nodes[n].next_id = 1
    now, prev = 1, 1
    for _ in range(n - 1):
        for i in range(m - 1):
            prev = now
            now = nodes[now].next_id
        print(nodes[now].id, end=' ')
        nodes[prev].next_id = nodes[now].next_id
        now = nodes[prev].next_id
    print(nodes[now].id)
