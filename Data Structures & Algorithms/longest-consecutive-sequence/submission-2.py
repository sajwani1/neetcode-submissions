class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Create a set of all the unique integers
        numSet = set(nums)
        longest = 0

        # Iterate through all elements of the set
        for num in numSet:
            # If num - 1 doesn't exist in the set,
            # this means this number is a possible starting value
            if (num - 1) not in numSet:
                length = 1
            
                # While the consective numbers exist in the set,
                # keep adding to the length
                while (num + length) in numSet:
                    length += 1
            
                # Get the longest consective sequence
                longest = max(length, longest)

        return longest


    # Time Complexity: O(n) since the array is only traversed once
    # Space Complexity: O(n) to hold the entire array in the hashset
    # if every element was unique
        