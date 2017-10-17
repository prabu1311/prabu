def sum(list):
    if len(list)== 1:
        return list[0]
    else:
        return list[0] + sum(list[1:3])
print(sum([5,7,3,8,11]))
