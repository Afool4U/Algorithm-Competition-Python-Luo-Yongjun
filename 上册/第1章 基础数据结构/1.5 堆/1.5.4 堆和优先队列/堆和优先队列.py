from heapq import heappush, heappop
# Python中的heapq模块实现了最小堆

if __name__ == '__main__':
    n = int(input())
    heap = []
    for _ in range(n):
        op = input().split()
        if op[0] == '1':
            heappush(heap, int(op[1]))
        elif op[0] == '2':
            print(heap[0])
        else:
            heappop(heap)
