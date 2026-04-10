class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows,cols=len(board),len(board[0])
        vis=[[False for _ in range(cols)] for _ in range(rows)]

        def dfs(r,c,i):
            if i==len(word):
                return True
            if(r<0 or c<0 or r>=rows or c>=cols or word[i]!= board[r][c] or vis[r][c]):
                return False

            vis[r][c]=True  #I’m currently using this cell in my path.
            res = (dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1))
            #“From this cell, can I complete the rest of the word in any direction?”

            vis[r][c]=False   #“I’m done exploring paths using this cell — now free it for other possibilities.”
            return res

        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True
        return False
        