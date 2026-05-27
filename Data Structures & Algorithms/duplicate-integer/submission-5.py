class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        elements = set()
        for num in nums:
            if num not in elements:
                elements.add(num)
            else:
                return True
        return False
        