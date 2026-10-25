def to_triplets(matrix):
    rows =len (matrix)
    cols= len(matrix[0])
    triplets = [[rows, cols, 0]]
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != 0:
                triplets.append([i,j,matrix[i][j]])
                triplets[0][2]+=1
                return to_triplets
            matrix=[
                [0,0,3,0],
                [0,0,0,0],
                [5,0,0,8]
            ]
            print(to_triplets(matrix))