from email import header, headerregistry


def isPalindrome(self,head: ListNode)->bool:
    #��ũ �ڷ��� ����
    q:Deque=collections.deque()

    if not head:#if not head: ������ �Է����� �־��� ���� ����Ʈ head�� ��������� ��� True�� ��ȯ�Ͽ� �ش� ����Ʈ�� �Ӹ�������� ó���մϴ�. 
        return True

    node=head
    while node is not None:
        q.append(node.val)
        node=node.next

    while len(q)>1:
        if q.popleft()!=q.pop():
            return False

    return True