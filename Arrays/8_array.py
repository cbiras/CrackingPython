"""
given a m*n matrix, if an element is 0, set to zero the row and column of that element
"""
def zero_matrix(mat):
    row = [0 for i in range(len(mat))]
    col = [0 for i in range(len(mat[0]))]

    for i in range(len(mat)):
        for j in range((len(mat[0]))):
            if mat[i][j] == 0:
                row[i]=1
                col[j] = 1
    for i in range(len(row)):
        if row[i]==1:
            make_zero_row(mat,i)
    for i in range(len(col)):
        if col[i]==1:
            make_zero_col(mat,i)
    return mat
def make_zero_row(mat,row):
    for i in range(len(mat[0])):
        mat[row][i] = 0

def make_zero_col(mat,col):
    for i in range(len(mat)):
        mat[i][col] = 0

if __name__=="__main__":
    mat = [[0,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    print(zero_matrix(mat))
