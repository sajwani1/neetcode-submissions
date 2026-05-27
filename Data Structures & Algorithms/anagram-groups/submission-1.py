class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)
        
        for str in strs:
            letters = [0] * 26
            for s in str:
                letters[ord(s) - ord('a')] += 1
            dict[tuple(letters)].append(str)

        return list(dict.values())



            


        