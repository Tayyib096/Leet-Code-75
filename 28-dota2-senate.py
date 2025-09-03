from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_queue = deque()
        d_queue = deque()

        for i, e in enumerate(senate):
            if e == 'R':
                r_queue.append(i)
            else:
                d_queue.append(i)

        n = len(senate)

        while r_queue and d_queue:
            if r_queue[0] < d_queue[0]:
                r_queue.append(r_queue[0]+n)
            else:
                d_queue.append(d_queue[0]+n)
            
            r_queue.popleft()
            d_queue.popleft()

        return "Radiant" if r_queue else "Dire"
