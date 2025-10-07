list1 = [1,2,3,4,5,6,7,8,9]
list2 = [1,3,5,7,9]
result = map(lambda x,y: x+y, list1, list2)
print(list(result))

def sq(x):
    return x*x
result2 = map(sq, list1)
print(list(result2))