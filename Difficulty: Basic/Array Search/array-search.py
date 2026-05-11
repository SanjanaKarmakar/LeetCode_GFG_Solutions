class Solution:
    def search(self, arr, x):
        # arr= [1, 2, 3, 4, 2, 10, 50]
        count=0
        for i in range(len(arr)):
            if arr[i]==x:
                return i
        
        return -1
              