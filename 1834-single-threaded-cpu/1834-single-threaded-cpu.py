class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        heap = [[tasks[i][0],i, tasks[i][1]] for i in range(len(tasks))]
        heapify(heap)
        store = []

        def addToStore(time):
            while heap and heap[0][0] <= time:
                enq_time, index, process_time = heappop(heap)
                heappush(store, [process_time, index])
        
        time = 0
        answer = []
        while heap or store:
            if (heap and not store) and time < heap[0][0]:
                time = heap[0][0]
            addToStore(time)
           
          
            process_time, index  = heappop(store)
            answer.append(index)
            time += process_time
    
        return answer


