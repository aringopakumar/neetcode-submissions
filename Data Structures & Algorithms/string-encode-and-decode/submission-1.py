class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ''
        for item in strs:
            result += item
            result += "012345"
        return result

    def decode(self, s: str) -> List[str]:
        final = s.split("012345")
        del final[-1]
        return final