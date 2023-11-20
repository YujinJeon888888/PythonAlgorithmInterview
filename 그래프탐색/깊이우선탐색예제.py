from ctypes.wintypes import CHAR


def dfs(graph, start, visited=None):
    if visited is None:#맨 초기상태면
        visited = set()#지금 방문할 집합 공간을 만들어준거임
    
    print(start)
    visited.add(start)
    
    for neighbor in graph[start]:#그 키값에 들어있는 리스트들을 쫙 방문해봄
        if neighbor not in visited:#방문 안 된거면
            dfs(graph, neighbor, visited)#방문한 목록에 넣어주고, 그 키값으로 또 밑으로 내려가봄. 호출한게 시행되면 다시 여기로 리턴됨(계속 내려가다가 없어서 리턴된다면, 그 부모노드 상태로 리턴되니까 할일없으면 위로 쫙쫙 올라가고 최상위노드의 다른 집합을 다시 탐색할거임. (여기선 A의 오른쪽집합들))

# 예제 그래프
graph = {#딕셔너리
    'A': ['B', 'C'],#A는 키, ['B','C']는 리스트
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C'],
    'G': ['C']
}


# 시작 정점을 'A'로 설정
N=input()
M=input()
R=input()


dfs(graph, 'A')
