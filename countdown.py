def countdown(num):
    numList = []
    for x in range(num,-1,-1):
       numList.append(x)
    return numList

print(countdown(5))