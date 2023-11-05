from email import header, headerregistry


def isPalindrome(self,head: ListNode)->bool:
    #데크 자료형 선언
    q:Deque=collections.deque()

    if not head:#if not head: 문장은 입력으로 주어진 연결 리스트 head가 비어있으면 즉시 True를 반환하여 해당 리스트를 팰린드롬으로 처리합니다. 
        return True

    node=head
    while node is not None:
        q.append(node.val)
        node=node.next

    while len(q)>1:
        if q.popleft()!=q.pop():
            return False

    return True