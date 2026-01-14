class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Solution1 (Brute Force)
        hmap = {}
        for s in strs:
            key = "".join(sorted(s))
            if key in hmap:
                hmap[key].append(s)
            else:
                hmap[key] = [s]

        return [x for x in hmap.values()]
