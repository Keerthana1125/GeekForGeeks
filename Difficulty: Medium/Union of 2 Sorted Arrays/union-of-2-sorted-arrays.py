class Solution:
    def findUnion(self, a, b):
        # code here 
        arr=a+b
        return sorted(set(arr))