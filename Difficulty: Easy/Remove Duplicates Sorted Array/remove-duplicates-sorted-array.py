class Solution:
    def removeDuplicates(self, arr):
        # code here 
        arr = list(dict.fromkeys(arr))
        return arr