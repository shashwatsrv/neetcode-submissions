class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHp,self.k=nums,k
        heapq.heapify(self.minHp)
        while len(self.minHp)>k:
            heapq.heappop(self.minHp)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.minHp,val)
        if len(self.minHp)>self.k:
            heapq.heappop(self.minHp)
        return self.minHp[0]
