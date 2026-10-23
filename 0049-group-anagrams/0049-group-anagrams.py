class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hmap = {}
        for s in strs:
            y = " ".join(sorted(s))
            if y not in hmap:
                hmap[y] = [s]
            else:
                hmap[y].append(s)
        result=[]
        for s in hmap:
            result.append(hmap[s])
        return result