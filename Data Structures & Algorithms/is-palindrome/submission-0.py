class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_text = ''.join(string.lower() for string in s if string.isalnum())
        return cleaned_text == cleaned_text[::-1]