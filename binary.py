def file(path):
    def mergeSort(arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]
            mergeSort(L)
            mergeSort(R)
            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
        return arr
    fhand = open(path, 'r')
    str = ''
    for line in fhand:
        str += line
    lst = str.split()
    lst = mergeSort(lst)
    return lst

def binarySearch(lst, l, r,x):
    if r>=l:
        mid = l+ int((r-l)/2)
        #check if x is present at mid
        if lst[mid]==x:
            return True
        #if x is greater, ignore left half
        elif lst[mid] >x:
            return(binarySearch(lst, l, mid-1,x))
        # if x is smaller, ignore right half
        else:
            return(binarySearch(lst, mid+1,r,x))
    else:
        #if we reach here then the element was not present
        return False
