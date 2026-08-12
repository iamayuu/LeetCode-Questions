class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        n = len(s)
        fs = ""
        count_bs = 0
        for i in range(n-1,-1,-1):
            if s[i]=="#":
                count_bs+=1
            else:
                if count_bs==0:
                    fs = s[i]+fs
                elif count_bs > 0:
                    count_bs -=1
                    continue
        
        n = len(t)
        ft = ""
        count_bs = 0
        for i in range(n-1,-1,-1):
            if t[i]=="#":
                count_bs+=1
            else:
                if count_bs==0:
                    ft = t[i]+ft
                elif count_bs > 0:
                    count_bs -=1
                    continue
            
        return fs==ft
        