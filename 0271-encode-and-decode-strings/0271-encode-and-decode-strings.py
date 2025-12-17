class Solution:

    def encode(self, strs: List[str]) -> str:
        size = ""
        size_arr = []
        data = ""
        for word in strs:
            size_arr.append(str(len(word)))
            data = data+word
        
        size = ",".join(size_arr)
        data = size+"#"+data

        return data


    def decode(self, s: str) -> List[str]:
        if s == "#":
            return []
        index = s.index("#")
        size_arr = s[:index].split(",")
        data = s[index+1:]
        result = []
        
        for i in size_arr:
            result.append(data[:int(i)])
            data = data[int(i):]
        
        return result
