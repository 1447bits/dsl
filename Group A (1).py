# Group A play -- Cricket
# Group B play -- Batminton
# Group C play -- Football







cricket = ["a", "b", "c"]
football = ["a", "b", "c", "e", "f"]
batminton = ["a", "b", "c", "d"]

def minus (lst1, lst2):
    lst = []
    for i in lst1:
        if i not in lst2:
            lst.append(i)
    for i in lst2:
        if i not in lst1:
            lst.append(i)
    return lst

def intersection (lis1, lis2):
    lst = []
    for i in lis1:
        if i not in lst:
            lst.append(i)
    return lst

def union (lst1, lst2):
    lst = lst1.copy()
    for i in lst2:
        if i not in lst:
            lst.append(i)
    return lst

def unionall (lst1, lst2, lst3):
    lst = lst1.copy()
    for i in lst2:
        if i not in lst:
            lst.append(i)
    for i in lst3:
        if i not in lst:
            lst.append(i)
    return lst

print ("No of students playing both cricket and batminton : ")
print (union(cricket, batminton), "\n")

print ("No of students playing cricket or batminton : ")
print (intersection(cricket, batminton), "\n")

print ("No of students playing Nither cricket Not batminton :")
all = unionall(cricket, batminton, football)
some = union(cricket, batminton)
nn = minus(all, some)
print (len(nn))

print ("No of students playing cricket and football not batminton :")
mm = minus(all, batminton)
print (mm)
print (len(mm))

















