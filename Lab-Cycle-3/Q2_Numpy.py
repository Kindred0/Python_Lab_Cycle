import numpy

row = int(input("Enter the number of variables\t: "))
coloumn = int(input("Enter the number of samples\t: "))

mat = []
for i in range(0,row) :
    mat_row = []
    for j in range(0,coloumn) :
        mat_row.append(int(input("Variable %d sample  %d \t: "% (i+1, j+1))))
    mat.append(mat_row)
mat = numpy.array(mat)

reduced_row = int(input("Enter the number of rows of the matrix to be redcuced into\t: "))
        
dimension = [row, coloumn]
print("Dataset Matrix\t:\n",mat)
#print("Dimension\t:\n",dimension)

def cov(x, y) :
    sum = 0
    for k in range(0, coloumn) :
        sum = sum + ((mat[x, k] - mean_vector[x]) * (mat[y, k] - mean_vector[y]))
    return sum

mean_vector = numpy.array([])
for i in mat :
    sum = 0
    for j in i :
        sum = sum + j
    mean = sum / coloumn
    mean_vector = numpy.append(mean_vector, mean)

print("Mean Vector\t:\n",mean_vector)

cov_mat = []

for i in range(0, row) :
    cov_row = []
    for j in range(0, row) :
        cov_row.append(cov(i,j))
    cov_mat.append(cov_row)
cov_mat = numpy.array(cov_mat)
print("Covarience Matrix\t:\n",cov_mat)


eigenvalues, eigenvectors = numpy.linalg.eig(cov_mat)
eigenvectors = numpy.transpose(eigenvectors)
print("Normalized Eigen Matrix\t:\n",eigenvectors)

variance_mat = []
for i in mat :
    for j in range(0 , row) : 
        variance_mat.append(i - mean_vector[j])
    break
variance_mat = numpy.array(variance_mat)
print("Variance Matrix\t:\n",variance_mat)

sum = 0
PCA_mat = []
for i in range(0, row) :
    PCA_row = []
    for j in range(0,coloumn) :
        sum = 0
        for k in range(0, row) :
            sum = sum + (eigenvectors[i, k] * variance_mat[k, j])
        PCA_row.append(sum)
    PCA_mat.append(PCA_row)

PCA_mat = numpy.array(PCA_mat)
reduced_mat = []
for i in range(0, row) :
    print("Principal Component",i+1,"\t:\n",PCA_mat[i])
    if reduced_row > i :
        reduced_mat.append(PCA_mat[i])

reduced_mat = numpy.array(reduced_mat)
print("Dimensionally Reduced Dataset\t:\n", reduced_mat)

#print("Principal Component Matrix\t:\n",PCA_mat)