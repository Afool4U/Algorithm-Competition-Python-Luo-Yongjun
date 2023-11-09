class Node:
    data = None
    next = None


if __name__ == '__main__':
    n, m = map(int, input().split())
    head = Node(); head.data = 1; head.next = None
    now = head
    for i in range(2, n + 1):
        p = Node(); p.data = i; p.next = None
        now.next = p
        now = p
    now.next = head

    now = head; prev = head
    for _ in range(n - 1):
        for i in range(m - 1):
            prev = now
            now = now.next
        print(now.data, end=' ')
        prev.next = now.next
        now = prev.next
    print(now.data)
