class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stk = []
        for index, temp in enumerate(temperatures):
            while stk and stk[-1][0] < temp:
                stored_index = stk.pop()[1]
                ans[stored_index] = index - stored_index
            stk.append((temp, index))
        return ans