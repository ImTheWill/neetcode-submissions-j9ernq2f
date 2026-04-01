class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        cubeMap = defaultdict(set)
        rowMap = defaultdict(set)
        columnMap = defaultdict(set)
        

        for i in range(len(board)):
            for j in range(len(board[i])):
                value = board[i][j]
                if value !=".":

                    #rowCheck
                    if value in rowMap[i]:
                        print("duplicate in row", i)
                        return False
                    else: rowMap[i].add(value)

                    #columnCheck
                    if value in columnMap[j]:
                        print("duplicate in column", j)
                        return False
                    else: columnMap[j].add(value)

                    #cubeCheck
                    index = (i//3)*3 + (j//3)
                    if value in cubeMap[index]:
                        print("duplicate in cube", index)
                        return False
                    else: cubeMap[index].add(value)

                else: continue


        return True;

                
            

