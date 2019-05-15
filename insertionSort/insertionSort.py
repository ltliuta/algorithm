def insertionSort(a, n):
    if(n < 1): return

    for i in range(1,n):
        j = i - 1
        tmp = a[i]

        while j >= 0:
            if a[j] > tmp:
                a[j+1] = a[j]
                j = j - 1
            else: break
        a[j+1] = tmp

    print 'after sort data:'
    print a

a = [9, 4, 3, 1, 5, 2, 6, 7, 8]
n = len(a)

print "test data:"
print a
insertionSort(a, n)

