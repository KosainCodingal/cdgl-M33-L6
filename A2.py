def flips(a):
    f0 = 0
    f1 = 0
    for i in a:
        if i == 0: f0+=1
        elif i == 1: pass
    for i in a:
        if i == 1: f1+=1
        elif i== 0 : pass
    return (f0, f1)

a = [0, 1, 1, 0, 1, 0, 1, 1]

print(flips(a)[0])
print(flips(a)[1])
