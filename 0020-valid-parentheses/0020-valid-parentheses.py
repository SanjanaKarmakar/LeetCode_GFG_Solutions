class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            False
        while "()" in s or "[]" in s or "{}" in s:
            s = s.replace("()", "")
            s = s.replace("[]", "")
            s = s.replace("{}", "")
        # If the string is empty, it was valid
        return s == ""