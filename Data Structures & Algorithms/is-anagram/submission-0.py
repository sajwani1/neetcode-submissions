class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        def dictCreator(str):
            dict = {}
            for char in str:
                if char in dict:
                    dict[char] += 1
                else:
                    dict[char] = 1
            return dict
        return dictCreator(s) == dictCreator(t)
        
        