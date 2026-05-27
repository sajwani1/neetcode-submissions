class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        # Sort the nums list
        nums.sort()

        # enumerate() function returns key value pairs where the key
        # is the index and the value is the actual value
        # So i = index and a = nums[i]
        for i, a in enumerate(nums):

            # If a is positive, there is no way to get 3 numbers
            # to add up to 0 since everything after a will be positive
            if a > 0:
                break

            # Skip duplicates by checking that the new number
            # is not equal to the previous number
            if i > 0 and a == nums[i - 1]:
                continue

            # Left pointer starts right after i
            l = i + 1
            # Right pointer starts at the end
            r = len(nums) - 1

            # Until the left and right pointers converge, calculate
            # the threeSum and keep moving the left and right pointers
            while l < r:
                threeSum = a + nums[l] + nums[r]
                
                # If the sum is greater than 0, decreasing the right
                # pointer will lower the sum
                if threeSum > 0:
                    r -= 1
                # If the sum is less than 0, increasing the left
                # pointer will make the sum greater
                elif threeSum < 0:
                    l += 1
                # If the sum is equal to 0, we have a triplet
                # to add to the result list
                else:
                    res.append([a, nums[l], nums[r]])
                    # Just shift the left pointer because the 
                    # loop will cause the right pointer to 
                    # automatically shift if necessary
                    l += 1

                    # Check if the new number the left pointer
                    # points to is a duplicate, and if so, shift
                    # it again, ensuring it is still less than the 
                    # right pointer
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res

        # Time Complexity: O(n^2) since the sorting takes O(nlogn) and
        # traversing the array twice, once for a and another time
        # for the pointers
        # Space Complexity: O(1) or O(n) depending on 
        # sorting algorithm

        