class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        min_heap = [-x for x in nums]
        heapq.heapify(min_heap)

        for i in range(k - 1):
            heapq.heappop(min_heap)
        
        return -1 * min_heap[0]