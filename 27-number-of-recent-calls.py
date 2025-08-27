class RecentCounter:

    def __init__(self):
        self.records = []
        self.time = 0        

    def ping(self, t: int) -> int:
        self.records.append(t)
        while self.records[self.time] < t - 3000:
            self.time +=1
        return len(self.records) - self.time
        