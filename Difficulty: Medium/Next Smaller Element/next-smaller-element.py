class Solution:
	def nextSmallerEle(self, arr):
		n = len(arr)
        result = [-1] * n
        stack = []
        for i in range(n):
            while stack and arr[i] < arr[stack[-1]]:
                index_to_update = stack.pop()
                result[index_to_update] = arr[i]
            stack.append(i)
        return result