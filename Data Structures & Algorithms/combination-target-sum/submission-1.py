class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        #                  [2]                            []
        #         [2, 2]              [2]             [3]    []
        # [2, 2, 2]   [2, 2]    [2, 3]    [2]

        # list of combination that keeps getting added to
        res = []
        # sort the nums so that once we hit a value
        # that doesn't work, we don't have to continue 
        # looking through the nums array since those
        # numbers will all be greater 
        nums.sort()

        # dfs takes in current value we are keeping the tree
        # as well as current list of elements, and their sum
        def dfs(i, curr, total):
            # if we reach total, add this combination to our res list
            if total == target:
                res.append(curr.copy())
                return

            # go through all possible nums to add next
            # from the ith pos till the end
            for j in range(i, len(nums)):
                # if the total is exceed, we don't need to 
                # continue checking the rest of the nums because
                # we know they are all greater
                if total + nums[j] > target:
                    return

                # otherwise, add this number
                curr.append(nums[j])
                # run dfs with the boundary of j, and add the
                # new number we are adding to the total
                dfs(j, curr, total + nums[j])
                # try the combination without this number
                # by just popping it to backtrack
                curr.pop()

        # start the dfs with nothing
        dfs(0, [], 0)
        return res

        # Time Complexity: O(2^t/m) where t is target and m
        # is the min value in nums because we are making 2 decisions
        # each time, and the height can be at most target
        # Space Complexity: O(t/m) because that is the maximum
        # depth of curr

        
        