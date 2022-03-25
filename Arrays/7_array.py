def rotate_matrix(mat):
    if len(mat)==0 or len(mat)!=len(mat[0]):
        print("empty or not squared")
        return False
    n = len(mat)
    for layer in range(n//2):
        first = layer
        last = n-1-layer
        for i in range(first,last):
            offset = i - first
            top = mat[first][i]
            
            mat[first][i] = mat[last-offset][first]

            mat[last-offset][first] = mat[last][last-offset]

            mat[last][last-offset] = mat[i][last]

            mat[i][last] = top
    print(mat)
    return True

if __name__=="__main__":
    mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    rotate_matrix(mat)

