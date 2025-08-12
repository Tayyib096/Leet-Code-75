class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        tracker = dict()

        for n in arr:
            if n not in tracker:
                tracker[n] = 1
            
            else:
                tracker[n]+=1

        return ( len(list(tracker.values())) == len(list(set(list(tracker.values())))) )