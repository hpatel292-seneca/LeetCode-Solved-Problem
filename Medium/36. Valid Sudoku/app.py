class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        hashtable={}
        for i in range(9):
            hashtable={}
            for j in range(9):
                if board[i][j]==".":
                    continue
                else:
                    if board[i][j]>9 or board[i][j]<1:
                        return False
                    elif board[i][j] in hashtable:
                        return False
                    else:
                        hashtable[board[i][j]]=1


        for i in range(9):
            hashtable={}
            for j in range(9):
                if board[j][i]==".":
                    continue
                else:
                    if board[j][i]>9 or board[j][i]<1:
                        return False
                    elif board[j][i] in hashtable:
                        return False
                    else:
                        hashtable[board[j][i]]=1
        return True

sol=Solution()
sol.isValidSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])