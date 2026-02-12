class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # for c in letters:
        #     if c>target:
        #         return c
        # return letters[0]
        
        return next((c for c in letters if c>target),letters[0])