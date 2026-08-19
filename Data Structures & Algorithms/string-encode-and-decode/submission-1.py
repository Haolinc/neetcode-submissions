class Solution:
    def encode(self, strs: List[str]) -> str:
        ans = ''
        for string in strs:
            ans += str(len(string)) + '#' + string
        return ans
    def decode(self, s: str) -> List[str]:
        index = 0
        ans = []
        while index < len(s):
            hash_index = s.find('#', index)
            str_num = int(s[index: hash_index])
            ans.append(s[hash_index + 1: hash_index + str_num + 1])
            index = hash_index + str_num + 1
        
        return ans