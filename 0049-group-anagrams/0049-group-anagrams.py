class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = defaultdict(list)

        for word in strs:
            key = "".join(sorted(word))
            groups[key].append(word)

        return list(groups.values())