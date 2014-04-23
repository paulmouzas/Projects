def merge(L1, L2):
    """ merges two ordered lists 
    into one ordered list  """
    ans = []
    while len(L1) != 0 and len(L2) != 0:
        if L1[0] <= L2[0]:
            ans.append(L1.pop(0))
        else:
            ans.append(L2.pop(0))
    if len(L1) > 0:
        ans += L1
    if len(L2) > 0:
        ans += L2
    return ans
    
def mergeSort(L):
    """ Orders a list of unordered
    elements with recursion """
    
    #base case
    if len(L) <= 1:
        return L

    mid = len(L)/2
    left = mergeSort(L[:mid])
    right = mergeSort(L[mid:])
        
    return merge(left, right)
        
if __name__ == '__main__':
    print mergeSort([4,6,43,6,6547,6,6,36,574,3,6,5])
