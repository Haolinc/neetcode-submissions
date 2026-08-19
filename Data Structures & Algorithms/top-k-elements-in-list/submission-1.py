class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = collections.Counter(nums)
        ans = []
        for key in freq.keys():
            heapq.heappush(ans, (freq[key], key))
            if len(ans) > k:
                heapq.heappop(ans)
        return [item[1] for item in ans]
