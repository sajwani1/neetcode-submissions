class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # Each task = [enqueueTime, processingTime]
        # For index, element in tasks
        for i, t in enumerate(tasks):
            # Add index as a 3rd element of each list in tasks
            # because our final return needs to be by index
            # For each task = [enqueueTime, processingTime, index]
            t.append(i)

        # Use the first element of each list in the tasks
        # list to sort the tasks (the enqueue time)
        tasks.sort(key=lambda t: t[0])

        res = []
        minHeap = []
        # Pointer to track which tasks have been considered
        i = 0
        # CPU time starts at first task's enqueue time
        time = tasks[0][0]

        while minHeap or i < len(tasks):
            # Check if the time is greater than any of the
            # enqueue times 
            while i < len(tasks) and time >= tasks[i][0]:
                # Add the element on to the minheap,
                # organized by processing time and index
                # so the heap picks the smallest processingTime first
                heapq.heappush(minHeap, [tasks[i][1], tasks[i][2]])

                i += 1
                    
            # If there is nothing in the minheap, jump to the next
            # enqueue time
            if not minHeap:
                time = tasks[i][0]
            # If there are tasks available, process the one
            # with the smallest processing time
            else:
                procTime, index = heapq.heappop(minHeap)
                # Increase the time by the task duration
                time += procTime 
                # Add the index of this task to the result array
                res.append(index)
        return res

    # Time Complexity: O(nlogn)
    # Space Complexity: O(n)

        