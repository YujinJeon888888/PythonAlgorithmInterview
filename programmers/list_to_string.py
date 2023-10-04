arr=['a','b','c']
def solution(arr:list[str]):
    string=""
    i=0
    for i in range(len(arr)):
        string+=arr[i]
        i+=1
  
    return string
print(solution(arr))
