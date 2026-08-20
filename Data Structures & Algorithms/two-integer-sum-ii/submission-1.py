class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for index in range(len(numbers)):
            diff = target - numbers[index]
            
            left = index + 1
            right = len(numbers) - 1
            while left <= right:
                mid = int(left + (right - left) / 2)
                if numbers[mid] == diff:
                    return [index + 1, mid + 1]
                if numbers[mid] < diff:
                    left = mid + 1
                else:
                    right = mid - 1
        return []
        

