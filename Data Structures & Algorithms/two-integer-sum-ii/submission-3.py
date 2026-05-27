class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pointer1 = 0
        pointer2 = len(numbers) - 1

        # Continue until the left pointer overtakes 
        while pointer1 < pointer2:
            currentSum = numbers[pointer1] + numbers[pointer2]
            
            # Since numbers are in order, if the sum is too big
            # decrease from the right side
            if currentSum > target:
                pointer2 -= 1
            # Otherwise decrease from the left side
            elif currentSum < target:
                pointer1 += 1
            # The sum with the number at index pointer1 and
            # the number at index pointer2 is equal to target
            # so return it
            else:
                return [pointer1 + 1, pointer2 + 1]
        return []
        