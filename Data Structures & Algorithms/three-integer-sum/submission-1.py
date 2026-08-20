class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedNum = sorted(nums)
        ans = []
        for index in range(0, len(sortedNum) - 2, 1):
            left = index + 1
            right = len(sortedNum) - 1
            while left < right:
                cur_sum = sortedNum[index] + sortedNum[left] + sortedNum[right]
                if cur_sum == 0:
                    ans_arr = [sortedNum[index], sortedNum[left], sortedNum[right]]
                    if ans_arr not in ans:
                        ans.append(ans_arr)
                    left += 1
                    right -= 1
                elif cur_sum > 0:
                    right -= 1
                else:
                    left += 1
        return ans