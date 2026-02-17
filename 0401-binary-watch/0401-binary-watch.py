class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        #Solution1  Brute Force
        if turnedOn>8:
            return []
        
        res = []
        for hour in range(12):
            for minute in range(60):
                hour_set_bit = 0
                n=hour
                while n>0:
                    n = n&(n-1)
                    hour_set_bit+=1
                min_set_bit = 0
                n=minute
                while n>0:
                    n = n&(n-1)
                    min_set_bit+=1
                if hour_set_bit+min_set_bit==turnedOn:
                    res.append(str(hour)+":"+str(minute).zfill(2))
        return res
                