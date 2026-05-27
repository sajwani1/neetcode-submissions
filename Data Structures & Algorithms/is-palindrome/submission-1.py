class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Create a new string without spaces and non alphanumeric
        new_str = ""
        for ch in s:
            if ch.isalnum():
                new_str += ch.lower()
        
        # Pointer 1 starts at start of string
        pointer1 = 0
        # Pointer 2 starts at end of string
        pointer2 = len(new_str) - 1

        while pointer1 < pointer2:
            # While the pointers move towwards eachother, and
            # the characters at the pointers are equal, 
            # keep moving the pointers
            if new_str[pointer1] == new_str[pointer2]:
                pointer1 += 1
                pointer2 -= 1
            else:
                # If 2 characters are not equal, this is not 
                # a palindrome
                return False
        return True

        # Time Complexity: O(n)
        # Space Complexity: O(n)
        