class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # # Solution 1
        # return Counter(s) == Counter(t)

        # if len(s) != len(t):
        #     return False
            
        # dictHash  = {}
        # for i in s:
        #     if i in dictHash:
        #         dictHash[i]=dictHash[i]+1
        #     else:
        #         dictHash[i]=1

        # for i in  t:
        #     if i in dictHash and dictHash[i]>0:
        #         dictHash[i]=dictHash[i]-1
        #     else:
        #         return False

        # return True

        return "".join(sorted(s))=="".join(sorted(t))
        
        


        
