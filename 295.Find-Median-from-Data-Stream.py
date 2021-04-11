from sortedcontainers import SortedList
import heapq
class MedianFinder:

    def __init__(self):
      self.arr = SortedList()
      self.n = 0
      
    def addNum(self, num: int) -> None:
        self.arr.add(num)
        self.n += 1
    def findMedian(self) -> float:
        if self.n%2 == 1:
            return self.arr[self.n//2]
        else:
            return (self.arr[self.n//2]+self.arr[self.n//2-1])/2     
