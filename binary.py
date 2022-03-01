def file(path):
    fhand = open(path,'r')
    str = ''
    for line in fhand:
        str += line
    lst = str.split()
    lst.sort()
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
