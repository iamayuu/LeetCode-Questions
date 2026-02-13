def case2helperfunc(s: str, ch1, ch2):
    hmap = dict()
    count_ch1 = 0
    count_ch2 = 0
    maxlen = 0
    for i,c in enumerate(s):
        if c != ch1 and c !=ch2:
            hmap.clear()
            count_ch1=0
            count_ch2=0
            continue

        if c==ch1:
            count_ch1+=1
        if c==ch2:
            count_ch2+=1
        
        if count_ch1==count_ch2:
            maxlen = max(maxlen, count_ch1+count_ch2)
        
        diff = count_ch1-count_ch2
        if diff in hmap:
            maxlen = max(maxlen, i-hmap[diff])
        else:
            hmap[diff]=i
    return maxlen

class Solution:
    def case2helperfunc(self, s: str, ch1, ch2):
        hmap = dict()
        count_ch1 = 0
        count_ch2 = 0
        maxlen = 0
        for i,c in enumerate(s):
            if c != ch1 and c !=ch2:
                hmap.clear()
                count_ch1=0
                count_ch2=0
                continue

            if c==ch1:
                count_ch1+=1
            if c==ch2:
                count_ch2+=1
            
            if count_ch1==count_ch2:
                maxlen = max(maxlen, count_ch1+count_ch2)
            
            diff = count_ch1-count_ch2
            if diff in hmap:
                maxlen = max(maxlen, i-hmap[diff])
            else:
                hmap[diff]=i
        return maxlen
            
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        ans = 0
        #Case1 - one char is making the longest substring
        crr_count = 0
        crr_char = s[0]
        for i in range(n):
            if s[i]==crr_char:
                crr_count+=1
            else:
                crr_char=s[i]
                crr_count=1
            ans = max(ans,crr_count)

        #Case2 - two distinct chars are making ans
        ans = max(ans, case2helperfunc(s, 'a' , 'b'))
        ans = max(ans, case2helperfunc(s, 'b' , 'c'))
        ans = max(ans, case2helperfunc(s, 'a' , 'c'))

        #Case3  - all three chars are used in making the longest substring
        countA = 0
        countB = 0
        countC = 0
        hashMap = dict()
        
        for i, c in enumerate(s):
            if c=='a':
                    countA+=1
            if c=='b':
                    countB+=1
            if c=='c':
                    countC+=1
            
            if countA==countB and countB==countC:
                ans = max(ans, countA+countB+countC)
            
            diffAB = countA-countB
            diffBC = countB-countC

            key = (diffAB, diffBC)

            if key in hashMap:
                ans = max(ans, i-hashMap[key])
            else:
                hashMap[key]=i

        return ans