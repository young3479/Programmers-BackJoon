def solution(arr):
    if not arr or len(arr) == 1:
        return [-1]
    
    min_num = min(arr)
    arr.remove(min_num)
    return arr