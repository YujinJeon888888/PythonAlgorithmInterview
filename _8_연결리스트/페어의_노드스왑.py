class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#값만 스왑
def swapPairs(self,head:ListNode)->ListNode:
    cur=head #cur: 노드의 헤드

    while cur and cur.next:#cur와 cur.next가 존재하는 동안
        #값만 교환
        cur.val, cur.next.val=cur.next.val,cur.val#서로 교환한다. 파이썬에서는 temp없어도 작동
        cur=cur.next.next#새로운 시작지점을 지정한다.
    return head#head반환은 곧 노드반환

#반복구조로 스왑 (값만 교환x 연결리스트 자체를 바꿈)
node4 = ListNode(4)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

def swapPairs2(self,head: ListNode)->ListNode:
    root=prev=ListNode(None)
    prev.next=head
    while head and head.next:#헤드와 헤드의 다음이 존재하는 동안
        #b가 a(head) 를 가리키도록 할당
        b=head.next
        head.next=b.next
        b.next=head

        #prev가 b를 가리키도록 할당
        prev.next=b

        #다음번 비교를 위해 이동
        head=head.next
        prev=prev.next.next
    return root.next

# 위에서 생성한 연결 리스트를 함수에 전달하고 결과를 받습니다.
result = swapPairs2(None, node1)

# 결과 연결 리스트를 출력합니다.
while result:
    print(result.val, end=" -> ")
    result = result.next
