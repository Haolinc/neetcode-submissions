class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dup_dict = defaultdict(list)
        for string in strs:
            sorted_str = "".join(sorted(string))
            dup_dict[sorted_str].append(string)        
        return list(dup_dict.values())