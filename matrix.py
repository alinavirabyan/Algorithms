a_1 = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
    ]
a_2 = [[1, 0, 0],
       [2, 8, 9],
       [0, 20, 1]]

list3 = [[0, 0, 0],
        [0,0,0],
         [0, 0,0]
         ]
for i in range(len(a_1)):
    for j in range(len(a_2)):
        for k in range(len(list3)):
            list3[i][j] += a_1[i][k] * a_2[k][j]
#print(list3)
b = []

for row in list3:
    b.append(row)
print(b)

