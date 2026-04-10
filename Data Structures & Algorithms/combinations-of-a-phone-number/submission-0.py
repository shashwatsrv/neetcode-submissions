class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res=[]

        char={
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def back(i,curr):
            if len(curr)==len(digits):
                res.append(curr)
                return
            for c in char[digits[i]]:
                back(i+1,curr+c)
        

        if digits:
            back(0,'')
        return res