from ctypes.wintypes import CHAR

def dfs(graph, start, visited=None):
    if visited is None:#맨 초기상태면
        visited = set()#지금 방문할 집합 공간을 만들어준거임
    
    print(start)
    visited.add(start)
    
    for neighbor in graph[start]:#그 키값에 들어있는 리스트들을 쫙 방문해봄
        if neighbor not in visited:#방문 안 된거면
            dfs(graph, neighbor, visited)#방문한 목록에 넣어주고, 그 키값으로 또 밑으로 내려가봄. 호출한게 시행되면 다시 여기로 리턴됨(계속 내려가다가 없어서 리턴된다면, 그 부모노드 상태로 리턴되니까 할일없으면 위로 쫙쫙 올라가고 최상위노드의 다른 집합을 다시 탐색할거임. (여기선 A의 오른쪽집합들))

#그래프
graph = dict()

# 시작 정점을 R로 설정
N=int(input())
M=int(input())
R=input()

for _ in range(M):#M번반복
    key, neighbor = input().split()  # 입력을 공백을 기준으로 나누어 key와 neighbor로 받음
    if key not in graph:
        graph[key] = []  # 처음으로 key를 만나면 빈 리스트를 생성
    graph[key].append(neighbor)  # 현재 key에 대한 neighbor를 리스트에 추가

dfs(graph, 'A')
