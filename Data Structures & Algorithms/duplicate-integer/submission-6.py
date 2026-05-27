class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Since sets can only contain one of an item, create a set so that
        # you can go through the list of nums and add them to the set one by one
        seen = set()

        for num in nums:
            # If the num is already in the set, this means it is a duplicate
            if num in seen:
                return True
            # Otherwise add the num to the set
            seen.add(num)
        return False
        
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        