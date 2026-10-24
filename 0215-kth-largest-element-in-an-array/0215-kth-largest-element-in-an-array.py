class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # min_heap = [-x for x in nums]
        # heapq.heapify(min_heap)

        # for i in range(k - 1):
        #     heapq.heappop(min_heap)
        
        # return -1 * min_heap[0]

        #--------------------------------#
        min_heap = nums[:k]
        heapq.heapify(min_heap)

        for x in nums[k:]:
            if x > min_heap[0]:
                heapq.heappushpop(min_heap, x)
        
        return min_heap[0]