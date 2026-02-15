class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        ans = []
        i = len(a)-1
        j = len(b)-1

        while i>=0 or j>=0 or carry==1:
            total = 0
            if i>=0:
                total = total+int(a[i])
                i=i-1
            if j>=0:
                total = total+int(b[j])
                j=j-1
            total = total+carry
            carry = total//2
            ans.append(str(total%2))

        return ''.join(ans[::-1])