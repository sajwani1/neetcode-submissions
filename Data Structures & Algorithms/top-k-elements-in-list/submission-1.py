class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        import heapq

        # {num: count}
        # Count frequency of every number
        freq = Counter(nums)

        # If k == number of elements in num, we just have to return all elements
        if k == len(freq):
            return list(freq.keys())

        # Min heap that keeps track of k most frequent elements
        # Items are stored in tuples (count, num)
        heap = []

        for num, count in freq.items():
            heapq.heappush(heap, (count, num))
            
            if len(heap) > k:
                # Once we have exceeded k elements, keep popping the smallest
                heapq.heappop(heap)

        # Return just the nums of the remaining items in the heap
        result = []
        for count, num in heap:
            result.append(num)

        return result

        # Time Complexity: O(nlogk)
        # Space Complexity: O(n + k)
        