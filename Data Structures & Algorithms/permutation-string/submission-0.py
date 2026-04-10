class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l=0
        r=len(s1)
        ds1={}
        ds2={}

        for ch in s1:
            if ch not in ds1:
                ds1[ch]=1
            else:
                ds1[ch]+=1

        for ch in s2[:len(s1)]:
            if ch not in ds2:
                ds2[ch]=1
            else:
                ds2[ch]+=1
        
        if ds1==ds2:
            return True
        
        l=0
        for r in range(len(s1),len(s2)):
            ds2[s2[r]]=ds2.get(s2[r],0)+1

            old=s2[l]
            ds2[old]-=1
            if ds2[old]==0:
                del ds2[old]
            l+=1

            if ds1==ds2:
                return True

        return False




