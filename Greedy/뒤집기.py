s = input()

def isNotVoid(x):
    return x != ""

newList1= list(filter(isNotVoid, s.split('0')))
newList2= list(filter(isNotVoid, s.split('1')))
print( min([len(newList1), len(newList2)]))