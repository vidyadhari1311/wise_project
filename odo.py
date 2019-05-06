n , m ,od= int(input()) ,int(input()) , []
num = str(n)
l = len(num)
for i in range(10 ** (l-1) ,10**l):
    if list(str(i)) == list(sorted(str(i))) and  len(set(str(i))) == len(str(i)):od.append(i)
l2 = len(od)
def is_odo(k):
    for i in range(l2):
        if od[i] == k:
            return 1
def prev_num(i  , j):
    if(i == od[0]):return od[(len(od))- j]
    else:return od[(od.index(i)) - j]
def next_num(i , j):
    if(od.index(i) + j) >= len(od):return od[(od.index(i)) + j - len(od)]
    return od[(od.index(i)) + j]
if(is_odo(n)):
    print("previous reading is",prev_num(n,1))
    print("next reading is ",next_num(n,1))
    print(prev_num(n,m))
    print(next_num(n,m))
else:
    print("invalid")

