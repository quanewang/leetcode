"""
class MovingAverage {
MovingAverage(int n)
void put(int item)
double movingAverage()
}
5 6 1 3 4, n = 3
"""

class moving_average:
    def __int__(self, n):
        self.n = n
        self.q = []
        self.total = 0

    def put(self, item):
        if len(self.q) == n:
            dropped = self.q.pop(0)
            self.total -= dropped
        self.q.append(item)
        self.total += item

    def movingAverage(self):
        if not self.q:
            return 0
        return self.total / len(self.q)
