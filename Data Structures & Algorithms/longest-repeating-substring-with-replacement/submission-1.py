class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Hashmap to count frequencies
        count = {} 
        # Longest substring length
        res = 0

        left = 0
        # Iterate through the string
        for right in range(len(s)):
            # Add one to the current frequency of the 
            # the element at the right index 
            # Return default value of 0 with get function
            # if the letter doesn't exist in the hashmap
            count[s[right]] = 1 + count.get(s[right], 0)

            # If size of current window minus the
            # max frequency of all letters in the window is
            # greater than the number of swaps we are allowed K,
            # then this window is no longer valid
            if (right - left + 1) - max(count.values()) > k:
                # Subtract the left pointer element from the 
                # frequency count
                count[s[left]] -= 1
                # Increase the left pointer to test the new window
                left += 1

            # Update max length with size of current window
            # if possible
            res = max(res, right - left + 1)

        return res

        # Time Complexity: O(n)
        # Space Complexity: O(m)