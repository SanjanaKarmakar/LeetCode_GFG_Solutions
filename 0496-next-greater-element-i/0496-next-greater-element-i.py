class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greater_map = {}
        stack = []
        # Process nums2 to find all next greater elements
        for num in nums2:
            # While the stack isn't empty and the current num is larger than the top
            while stack and num > stack[-1]:
                # Pop the element and map it to the current num
                smaller_num = stack.pop()
                greater_map[smaller_num] = num
            # Push current num to stack
            stack.append(num)
        # Build the result for nums1 using the map
        # If num isn't in map, it means there was no greater element to its right
        return [greater_map.get(num, -1) for num in nums1]