class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, n in enumerate(nums):
            difference = target - n
            if difference in dict:
                return [dict[difference], i]
            else:
                dict[n] = i
        
 


        