class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nodup_nums = set(nums)
        ans = 0
        for num in nums:
            if (num - 1) not in nodup_nums:
                counter = 1
                while num + counter in nodup_nums:
                    counter += 1
                ans = max(counter, ans)
        return ans
