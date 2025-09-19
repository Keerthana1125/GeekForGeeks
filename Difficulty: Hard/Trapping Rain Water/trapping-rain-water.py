
class Solution:
    def maxWater(self, arr):
        # code here
        n = len(arr)
        if n == 0:
            return 0
        
        left, right = 0, n - 1
        max_left, max_right = 0, 0
        water = 0
        
        while left < right:
            if arr[left] < arr[right]:
                if arr[left] >= max_left:
                    max_left = arr[left]
                else:
                    water += max_left - arr[left]
                left += 1
            else:
                if arr[right] >= max_right:
                    max_right = arr[right]
                else:
                    water += max_right - arr[right]
                right -= 1
        
        return water