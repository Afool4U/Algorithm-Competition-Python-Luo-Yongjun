N = 105


class Node:
    id = None
    # data = None
    next_id, prev_id = None, None


nodes = [Node() for _ in range(N)]

if __name__ == '__main__':
    n, m = map(int, input().split())
    nodes[0].next_id = 1
    for i in range(1, n + 1):
        nodes[i].id = i
        nodes[i].prev_id = i - 1
        nodes[i].next_id = i + 1
    nodes[n].next_id = 1
    nodes[1].prev_id = n
    now = 1
    for _ in range(n - 1):
        for i in range(m - 1):
            now = nodes[now].next_id
        print(nodes[now].id, end=' ')
        prev = nodes[now].prev_id
        next = nodes[now].next_id
        nodes[prev].next_id = nodes[now].next_id
        nodes[next].prev_id = nodes[now].prev_id
        now = next
    print(nodes[now].id)
