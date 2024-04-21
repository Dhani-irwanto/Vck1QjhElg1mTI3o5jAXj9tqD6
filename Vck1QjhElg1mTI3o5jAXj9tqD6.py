temp = 1
kim = 3

result = 1
for i in range(kim):
    temp = 1
    print("repeat", result, "times")
    for i in range(result):
        print(temp, "+", kim, "=")
        temp = temp+kim
        print(temp)
    result = temp
    print("result = ", result)