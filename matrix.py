m1 = [[1,2,3],[4,5,6],[7,8,9]]
m2 = [[1,2,3],[4,5,6],[7,8,9]]
result = [[0,0,0],[0,0,0],[0,0,0]]

#function for matrix addition
def matrixAdditon(m1,m2):
    if(len(m1)!=len(m2)):
        print("Your Matrix can not be Added")
    else:
        for i in range(len(m1)):
            for j in range(len(m2)):
                result[i][j] = m1[i][j] + m2[i][j]
    return result
#Function for matrix subtraction
def matrixSubtraction(m1,m2):
    if(len(m1)!=len(m2)):
        print("Your Matrix can not be Subtracted")
    else:
        for i in range(len(m1)):
            for j in range(len(m2)):
                result[i][j] = m1[i][j] - m2[i][j]
    return result  
        

#function for matrix multiplication
def matrixMultiplication(m1,m2):
    if(len(m1[0])!= len(m2)):
        print("Your matrix can not be multipled!!")
    else:    
        for i in range(len(m1)):
            for j in range(len(m1[0])):
                for k in range(len(m2)):
                    result[i][j] += m1[i][k]*m2[k][k] 
    return result
#function for printing matrix    
def matrixprint(matrix):
    for i in matrix:
        print(i)
a = matrixAdditon(m1,m2)
matrixprint(a)
b = matrixSubtraction(m1,m2)
matrixprint(b)
c = matrixMultiplication(m1,m2)
matrixprint(c)

