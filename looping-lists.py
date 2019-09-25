list1 = [19,29,39,49,[11,22,33,44],['hello', 'bye', True, False, None]]

length = len(list1)
for i in range(length):
    if type(list1[i]) == int:
        print(list1[i])
        continue
    for j in range(len(list1[i])):
        print(list1[i][j])
