class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If the lengths are not the same, they cannot be anagrams
        if len(s) != len(t):
            return False

        # Create a list of size 26 initialized with all zeros
        count = [0] * 26
        for i in range(len(s)):
            # Determines the letter based on subtracting that elements unicode
            # from the unicode of 'a'
            # Increments the count for that letter if its in s 
            count[ord(s[i]) - ord('a')] += 1
            # Decrements the count for that letter if its in t
            count[ord(t[i]) - ord('a')] -= 1

        # If count is not all zeros, this means s and t are not anagrams
        for val in count:
            if val != 0:
                return False
        return True

        # Time Complexity: O(m + n)
        # Space Complexity: O(1)
        