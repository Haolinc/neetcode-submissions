class Solution:
    def __init__(self):
        self.encoded_str = ""
        self.decoded_list = {}
    def encode(self, strs: List[str]) -> str:
        self.decoded_list = strs
        return ""
    def decode(self, s: str) -> List[str]:
        self.encoded_str = s
        return self.decoded_list