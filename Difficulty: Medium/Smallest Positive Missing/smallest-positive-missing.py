class Solution:
    def missingNumber(self, arr):
        # code here
        arr.sort()
        res=1
        for num in arr:
            if num==res:
                res+=1
            elif num>res:
                break
        return res