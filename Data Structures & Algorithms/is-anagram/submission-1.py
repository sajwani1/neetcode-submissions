class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
            
        def frequencyCount(word):
            dict = {}
            for char in word:
                if char in dict:
                    dict[char] += 1
                else:
                    dict[char] = 1
            return dict
        
        if frequencyCount(s) == frequencyCount(t):
            return True
        return False
        