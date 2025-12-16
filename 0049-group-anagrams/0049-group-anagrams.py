class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ans = []
        dictHashMap = {}
        
        for word in strs:
            if "".join(sorted(word)) in dictHashMap:
                ans[dictHashMap["".join(sorted(word))]].append(word)
            else:
                ans.append([word])
                dictHashMap["".join(sorted(word))] = len(ans)-1

        return ans

        