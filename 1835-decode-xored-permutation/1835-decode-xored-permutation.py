class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        #Solution1
        # n = len(encoded)+1
        # perm = []
        # total = 0
        # for i in range(1, n+1):
        #     total ^= i
        # #finding the perm[0]
        # oddIndexTotal = 0
        # for oddIndex in range(1, len(encoded), 2):
        #     oddIndexTotal ^=encoded[oddIndex]
        
        # perm.append(total ^ oddIndexTotal)
        # for j in range(len(encoded)):
        #     perm.append(perm[j] ^ encoded[j])
        # return perm

        #Solution2 (Optimising the Total XOR Sum calculation)
        n = len(encoded)+1
        perm = []
        total = 0
        if n%4==0:
            total = n
        elif n%4==1:
            total = 1
        elif n%4==2:
            total = n+1
        elif n%4==3:
            total = 0
        #finding the perm[0]
        oddIndexTotal = 0
        for oddIndex in range(1, len(encoded), 2):
            oddIndexTotal ^=encoded[oddIndex]
        
        perm.append(total ^ oddIndexTotal)
        for j in range(len(encoded)):
            perm.append(perm[j] ^ encoded[j])
        return perm
