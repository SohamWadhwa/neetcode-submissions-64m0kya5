class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "e@#e"
        encoded = strs[0]
        for s in strs[1:]:
            encoded = encoded + "p@@p" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        if s == "e@#e":
            return []
        decoded = []
        decoded = s.split('p@@p')
        return decoded