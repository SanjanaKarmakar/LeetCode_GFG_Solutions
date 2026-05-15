class Solution:
    def maxSubarraySum(self, arr, k):
        current_sum = sum(arr[:k])
        max_sum = current_sum
        for i in range(k, len(arr)):
            current_sum += arr[i] - arr[i - k]
            if current_sum > max_sum:
                max_sum = current_sum
        return max_sum