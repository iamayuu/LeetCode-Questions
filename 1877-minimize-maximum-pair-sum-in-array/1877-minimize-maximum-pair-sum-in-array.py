class Solution:
    def minPairSum(self, a: List[int]) -> int:
        return max(map(add,b:=sorted(a),b[::-1]))