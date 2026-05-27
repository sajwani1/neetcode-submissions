class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initialize the result array with all 1s by default
        res = [1] * len(nums)
        
        prefix = 1

        # Modify the array to be a prefix array where each 
        # index holds the product of all numbers before it
        for i in range(len(nums)):
            # Update the result array first
            res[i] = prefix

            # Then multiply the current number with the product
            # of all the previous numbers, to serve as the prefix
            # of the next number
            prefix *= nums[i]

        # Instead of creating a seperate prefix and postfix array, 
        # just modify the result array itself
        postfix = 1

        # Modify the array to add in the postfixes by iterating
        # through backwards, where each index holds the product 
        # of all numbers after it
        for i in range(len(nums) - 1, -1, -1):
            # Update the result array by taking the current prefix
            # value and multiplying it by the postfix
            res[i] *= postfix

            # Then multiply the current number with the product
            # of all the succeding numbers, to serve as the postifx
            # of the number right before
            postfix *= nums[i]

        # Now each element in the array represents the product
        # of every number except for it
        return res

        # Time Complexity: O(n) since the entire array is traversed
        # Space Complexity: O(1) extra space, but O(n) for the output
        # array since we update all values directly in that