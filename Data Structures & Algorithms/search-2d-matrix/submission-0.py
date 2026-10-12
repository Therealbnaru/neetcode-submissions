class Solution:
	def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
            startElement = (0)
            endElement = len(matrix) * len(matrix[0]) - 1	
            middle = 0
            while(startElement <= endElement):
                middle = (startElement + endElement)//2
                i = middle// len(matrix[0]) 
                j = middle % len(matrix[0])
                if(matrix[i][j] > target):
                    endElement = middle - 1
                elif(matrix[i][j] < target):
                    startElement = middle + 1
                else:
                    return True

            return False 
