1.
def myreduce(function, *args):
    if len(args) == 0:
        return "Iterable has no elements"
    res = args[0]
    for i in range(1,len(args)):
        res = function(res,args[i])
    return res
reduce(lamda x,y:x+y, 1,2,3,4)

2.
def myfilter(function, seq):
    res = [i for i in seq if function(i)]
    return res
def func(n):
    if n!=2:
        return True
    else:
        return False
print(myfilter(func,[1,2,3,2,4,3]))

3.
l = ["x","y","z"]
res = [i*j for i in l for j in range(1,5)]       
print(res)


4.
l = ["x","y","z"]
res = [i*j for j in range(1,5) for i in l]       
print(res)

6.
res = [(j,i) for i in range(1,4) for j in range(1,4)]
print(res)


5.
l = [2,3,4]
l2 = l+[l[i]+1 for i in range(len(l))]+[l[i] + 2 for i in range(len(l))]
res = [[i] for i in l2]

l = [2,3,4,5]
l2 = [l]+[[l[i]+1 for i in range(len(l))]]+[[l[i] + 2 for i in range(len(l))]]+[[l[i] + 3 for i in range(len(l))]]
print(res,l2)





