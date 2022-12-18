import heapq

heap = []
heapq.heapify(heap)

with open("d1in.txt", "r") as inp:
    elfSum = 0
    for line in inp.readlines():
        if line != '\n':
            elfSum += int(line)
        else:
            heapq.heappush(heap, -elfSum)
            elfSum = 0
print(-sum([heapq.heappop(heap) for _ in range(3) ]))
