class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        #Solution1 Brute Force
        if len(queries[0])<=2:
            return queries
        ans = []
        for word in queries:
            if word in dictionary:
                ans.append(word)
            else:
                for dic in dictionary:
                    matched = 0
                    i = 0
                    for i in range(len(word)):
                        if word[i]==dic[i]:
                            matched+=1
                        if matched>=(len(word)-2):
                            break
                    if matched>=(len(word)-2):
                            ans.append(word)
                            break

        return ans