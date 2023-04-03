def inversmatriks(a):
    n = len(a)
    P = [[0.0 for i in range(len(a))] for j in range(len(a))]
    for i in range(3):
        for j in range(3):
            P[j][j] = 1.0
    for i in range(len(a)):
        a[i].extend(P[i])
    #main loop Gauss mulai di sini
    for k in range(n):
        if abs(a[k][k]) < 1.0e-12:
            for i in range(k+1, n):
                if abs(a[i][k]) > abs(a[k][k]):
                    for j in range(k, 2*n):
                        a[k][j], a[i][j] = a[i][j], a[k][j] #tuker baris
                    break
        pivot = a[k][k] 
        if pivot == 0: 
            print("This matrix is not invertible.")
            return
        else:
            for j in range(k, 2*n): 
                a[k][j] /= pivot
            for i in range(n): 
                if i == k or a[i][k] == 0: continue
                factor = a[i][k]
                for j in range(k, 2*n):
                    a[i][j] -= factor * a[k][j]
    for i in range(len(a)):
        for j in range(n, len(a[0])):
            print(a[i][j], end = " ")
        print()
a = [0, 2, 1], [4, 0, 1], [-1, 2, 0]
inversmatriks(a)
#panggil fungsi defnya dan definsikan bentuk matriks ke dalam array