import heapq

n = int(input())

heap = []
for i in range(n):
    data = int(input())
    heapq.heappush(heap,data)

result = 0

while len(heap) != 1:
    one = heap.heappop(heap)
    two = heap.heappop(heap)
    sum_value = one + two
    result += sum_value
    heapq.heappush(heap, sum_value)

print(result)