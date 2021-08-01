def valueGreaterThanSecond(num):
    newList = []
    if len(num) < 2:
        return False
    else:
        for x in num:
            if x > num[1]:
                newList.append(x)
        print("num length: ", len(newList))
        return newList

print(valueGreaterThanSecond([5,2,3,2,1,4]))
print("\n")
print(valueGreaterThanSecond([3]))