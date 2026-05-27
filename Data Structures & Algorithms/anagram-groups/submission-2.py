class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a dictionary initialized with lists
        dict = defaultdict(list) 
        
        for str in strs:
            # For each string, 
            # create a key with the count of each letter
            letters = [0] * 26
            for s in str:
                # ord() = asci value
                letters[ord(s) - ord('a')] += 1
            # Use tuple because a list cannot be a key
            # Append the word to the dictionary value list if it 
            # has the same frequencies of letters
            dict[tuple(letters)].append(str)

        return list(dict.values())