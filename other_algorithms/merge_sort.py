def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        l = arr[:mid]
        r = arr[mid:]
        
        # split it until two arrays of single element
        merge_sort(l)
        merge_sort(r)
        
        i = j = k = 0
	
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                arr[k] = l[i]
                i+=1
            else:
                arr[k] = r[j]
                j+=1
            k+=1
        
        while i < len(l):
            arr[k] = l[i]
            i+=1
            k+=1
            
        while j < len(r):
            arr[k] = r[j]
            j+=1
            k+=1
    return(arr)
            
            
print(merge_sort([1,2,3,-1]))

