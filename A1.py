def eqPoint(a):
    ls, rs = 0, 0
    n = len(a)

    for i in range(n):
        ls, rs = 0, 0
        
        for j in range(i): ls += a[j]
        for j in range(i+1, n): rs += a[j]
        if ls == rs: return i

    return None

arr = [-4, 6, 2, 0, 0, 1, 1]
print("element that reaches equilibrium:", eqPoint(arr))
