class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s= s.split()
        if len(pattern) != len(s):
            return False
        hmap = {}
        seen = set()
        for pat,word in zip(pattern,s):
            if pat in hmap:
                if hmap[pat] != word:
                    return False
            else:
                if word in seen:
                    return False
                hmap[pat] = word
                seen.add(word)
        return True