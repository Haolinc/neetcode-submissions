class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for index, num in enumerate(nums):
            if num > 0:
                break
            if index > 0 and nums[index] == nums[index - 1]:
                continue
            left = index + 1
            right = len(nums) - 1
            while left < right:
                cur_sum = nums[index] + nums[left] + nums[right]
                if cur_sum == 0:
                    ans_arr = [nums[index], nums[left], nums[right]]
                    if ans_arr not in ans:
                        ans.append(ans_arr)
                    left += 1
                    right -= 1

                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif cur_sum > 0:
                    right -= 1
                else:
                    left += 1
        return ans