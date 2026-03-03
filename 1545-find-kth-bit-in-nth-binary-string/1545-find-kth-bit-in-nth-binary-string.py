def cal_S(n):
    if n==1:
        return "0"
    else:
        S_n_1 = cal_S(n-1)
        invert_S_n_1 = ""
        for c in S_n_1:
            if c=="0":
                invert_S_n_1+="1"
            else:
                invert_S_n_1+="0"
        
        S = S_n_1+"1"+invert_S_n_1[::-1]
        return S

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        #Solution 1 (Brute Force)
        S = cal_S(n)
        return S[k-1]
