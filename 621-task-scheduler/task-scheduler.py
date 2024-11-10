class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        heap = []
        cooldown = [] ## (task_count,time), time= the next timer the task is available to run
        timer = 0
        for key,value in freq.items():
            heapq.heappush(heap,-value)
        
        while heap or cooldown:
            if heap:
                task= -heapq.heappop(heap)
                if task>1:
                    cooldown.append((task-1,timer+n+1))
            timer+=1
            while cooldown and cooldown[0][1]==timer:
                task_count, next_available = cooldown.pop(0)
                heapq.heappush(heap,-task_count)
        return timer