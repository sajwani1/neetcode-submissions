class Solution:

    def encode(self, strs: List[str]) -> str:
        # Create an empty string
        res = ""

        # For each string in the array, encode it in this format:
        # length#string
        for s in strs:
            res += str(len(s)) + "#" + s
        
        # Return the encoded string
        return res

    def decode(self, s: str) -> List[str]:
        # Create an empty list and pointer to traverse the string
        res = []
        i = 0

        while i < len(s):
            j = i

            # Keep moving j forward until we see a #
            while s[j] != '#':
                j += 1

            # The characters between i and j represent the length
            length = int(s[i:j])

            # Move i to the character right after the #
            i = j + 1
            # Move j forward length characters, representing the string
            j = i + length

            # Append the extracted string to the result list
            res.append(s[i:j])
            
            # Reset i by moving it forward to j to start
            # decoding the next string
            i = j
        
        return res

    # Time Complexity: O(m) since the entire string must be traversed
    # Space Complexity: O(m + n) to store the resulting
    # string and list