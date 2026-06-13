class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minh=[]
        for x,y in points:
            d=(x**2)+(y**2)
            minh.append([d,x,y])
        
        heapq.heapify(minh)
        res=[]
        while k>0:
            d,x,y=heapq.heappop(minh)
            res.append([x,y])
            k-=1
        return res
        
        