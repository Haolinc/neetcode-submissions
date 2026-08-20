class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nodup_nums = set(nums)
        visited = set()
        ans = 0
        for num in nums:
            if num in visited:
                continue
            counter = 1
            incrementing_num = num
            visited.add(num)
            while incrementing_num + 1 in nodup_nums:
                visited.add(incrementing_num)
                counter += 1
                incrementing_num += 1
            ans = max(ans, counter)
        return ans
