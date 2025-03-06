arr = [-1, 8, 9, 6, 7, 1]
target = 9

for index in range(len(arr)):
    if arr[index] == target:
        print(f"Տարրը գտնվել է ինդեքսում՝ {index}")
        break
else:
    print("Տարրը չի գտնվել զանգվածում")
