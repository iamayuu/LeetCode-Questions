class Solution:
    def rotatedDigits(self, n: int) -> int:
        #Brute Force
        hmap = {'0':'0', '1':'1', '2':'5', '5':'2', '6':'9', '9':'6', '8':'8'}
        def checkGood(num):
            temp = ""
            snum = str(num)
            if '3' in snum or '4' in snum or '7' in snum:
                return False

            for digit in snum:
                temp+=hmap[digit]

            return temp!=snum

        goodNums = 0
        for i in range(1,n+1):
            goodNums+= 1 if checkGood(i) else 0

        return goodNums