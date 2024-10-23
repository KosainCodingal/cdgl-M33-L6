def subArraySum(a, s):
    for i in range(len(a)):
        cs = arr[i]
        j = i+1
        while j <= len(a):
            if cs == s:
                print("SUM found b/w:")
                print("Indexes % d and % d"%(i, j-1))
                return True
            if cs > s or j == len(a):
                break
            cs += arr[j]
            j+= 1
    print("No sub array found")
    return False

arr = [
    3,6,2,2,56,1,0,9]
s = 10
sumArraySum(a, s)