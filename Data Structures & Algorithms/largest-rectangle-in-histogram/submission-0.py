class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        stk=[]
        max_ar=0

        for i,ht in enumerate(heights):
            start=i
            while stk and ht<stk[-1][0]:
                h,j=stk.pop()
                w=i-j
                a=h*w
                max_ar=max(max_ar,a)
                start=j
            stk.append((ht,start))
        
        while stk:
            h,j=stk.pop()
            w=n-j
            max_ar=max(max_ar,h*w)
        
        return max_ar
            