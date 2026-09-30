class TimeMap:

    def __init__(self):
        # {key : [[value, timestamp]]}
        self.hashmap = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        # add the key to the hashmap and initialize it 
        # with an empty list if doesn't exist
        if key not in self.hashmap:
            self.hashmap[key] = []
        # add the value and timestamp as a pair to the values list
        self.hashmap[key].append([value, timestamp])

        
    def get(self, key: str, timestamp: int) -> str:
        # default value to return if there are no values at
        # less than or equal to timestamp
        res = ""

        # get the list of value, timestamp pairs for this key
        values = self.hashmap.get(key, [])

        # use binary search to find the time that
        # is less than or equal to the timestamp we are given
        l, r = 0, len(values) - 1
        while l <= r:
            mid = (l + r) // 2
            if values[mid][1] == timestamp:
                return values[mid][0]
            elif values[mid][1] <= timestamp:
                # store this time as the closest time lower than
                # timestamp so far
                res = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1

        return res

    # Time Complexity: 
    # - set(): O(1) because we are just adding this key value pair in
    # - get(): O(log n) because we used a binary search
    # Space Complexity: O(m * n) where m is number of keys and n
    # is number of values associated with a key since we have a hashmap
    # to store every relationship

            
        
