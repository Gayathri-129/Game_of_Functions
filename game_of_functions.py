def my_fun(lst):
    total=0
    for i in range(len(lst)):
        total+=lst[i]
    print(total)

lst=[8,2,3,0,7]
my_fun(lst)