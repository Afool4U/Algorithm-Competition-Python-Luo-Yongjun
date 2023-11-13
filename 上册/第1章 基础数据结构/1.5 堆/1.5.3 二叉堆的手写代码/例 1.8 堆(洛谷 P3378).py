N = int(1e6 + 5)
heap = [0] * N
size = 0


def push(x: int) -> None:
    global size
    size += 1
    heap[size] = x
    i = size
    while i > 1 and heap[i] < heap[i // 2]:
        heap[i], heap[i // 2] = heap[i // 2], heap[i]
        i //= 2


def pop() -> None:
    global size
    heap[1] = heap[size]  # 将最后一个元素放到堆顶
    size -= 1
    i = 1
    while 2 * i <= size:  # 至少有左儿子
        son = 2 * i
        if son < size and heap[son + 1] < heap[son]:
            son += 1
        if heap[son] < heap[i]:
            heap[son], heap[i] = heap[i], heap[son]
            i = son
        else:
            break


if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        op = input().split()
        if op[0] == '1':
            push(int(op[1]))
        elif op[0] == '2':
            print(heap[1])
        else:
            pop()
