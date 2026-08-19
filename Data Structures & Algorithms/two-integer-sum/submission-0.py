class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexMap = {}
        for index in range(len(nums)):
            num = nums[index]
            if (target - num) in indexMap:
                return [indexMap[target - num], index]
            indexMap[num] = index
        return []
