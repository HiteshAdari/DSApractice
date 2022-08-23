
def searchMatrix(matrix, target: int) -> bool:
    def rowbin(matrix):
        left =0
        right =len(matrix)
        while left<right:
            mid=(left+right)//2
            if matrix[mid][0] > target:
                right = mid-1
            else:
                left = mid+1
        return left

    def colbin(midr):
        ar = matrix[midr]
        left = 0
        right = len(ar)
        while left <= right:
            mid = (left+right)//2
            if ar[mid] == target:
                return True
            elif ar[mid] > target:
                right = mid-1
            else:
                left = mid +1
        return False
    return colbin(rowbin(matrix))

print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3))






