class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store numbers as keys 
        # and their indexes as values
        dict = {}

        for i in range(len(nums)):
            # Calculate complement to determine if it is in the nums array
            complement = target - nums[i]
            if complement in dict:
                # Return the index of the number that we found
                return [dict[complement], i]
            # Add this number to the dictionary, so we can see if it is 
            # the complement of another number
            dict[nums[i]] = i
        # Base case return empty list
        return []

        # Time Complexity: O(n)
        # Space Complexity: O(n)
        