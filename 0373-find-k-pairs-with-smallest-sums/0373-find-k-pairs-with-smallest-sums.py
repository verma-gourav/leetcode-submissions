class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        if not nums1 or not nums2 or k == 0:
            return []

        min_heap = []
        res = []

        for j in range(min(len(nums2), k)):
            init_sum = nums1[0] + nums2[j]
            heapq.heappush(min_heap, (init_sum, 0, j)) 
        
        while len(res) < k:
            curr_sum, i, j = heapq.heappop(min_heap)
            res.append([nums1[i], nums2[j]])

            if i + 1 < len(nums1):
                next_sum = nums1[i + 1] + nums2[j]
                heapq.heappush(min_heap, (next_sum, i + 1, j))
        
        return res