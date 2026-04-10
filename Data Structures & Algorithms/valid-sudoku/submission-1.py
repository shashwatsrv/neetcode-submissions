class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if(self.checkr(board)==True and self.checkc(board)==True and self.tbt(board)==True):
            return True
        else:
            return False
    
    def checkr(self,board):
        for r in board:
            seenr=[]
            for i in r:
                if(i=="."):
                    continue
                if i in seenr:
                    return False
                elif(int(i)>9 or int(i)<1):
                    return False
                else:
                    seenr.append(i)
        return True
    
    def checkc(self,board):
        for c in range(len(board)):
            seenl=[]
            for r in range(len(board)):
                j=board[r][c]
                if j==".":
                    continue
                if (j in seenl):
                    return False
                elif(int(j)>9 or int(j)<1):
                    return False
                else:
                    seenl.append(j)
        return True
    
    def tbt(self,board):
        for r in range(0,9,3):
            for c in range(0,9,3):
                seenb=[]
                for i in range(3):
                    for j in range(3):
                        k=board[r+i][c+j]
                        if k==".":
                            continue
                        if k in seenb:
                            return False
                        elif(int(k)>9 or int(k)<1):
                            return False
                        else:
                            seenb.append(k)
        return True
    
                






                