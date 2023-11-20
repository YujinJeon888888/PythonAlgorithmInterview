def solution(tickets):
    answer = []

    # 그래프 생성
    graph = {}
    for ticket in tickets:
        start, end = ticket
        if start in graph:
            graph[start].append(end)
        else:
            graph[start] = [end]

    # 도착지 알파벳 역순으로 정렬
    for key in graph:
        graph[key].sort(reverse=True)

    # DFS 함수
    stack = ["ICN"]
    while stack:
        current = stack[-1]

        # 만약 현재 위치에서 갈 수 있는 곳이 없다면 경로에 추가
        if current not in graph or len(graph[current]) == 0:
            answer.append(stack.pop())
        else:
            # 갈 수 있는 곳이 있다면 스택에 추가하고 해당 간선 제거
            stack.append(graph[current].pop())

    # 경로 역순으로 반환
    answer.reverse()

    return answer